import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { STLLoader } from "three/addons/loaders/STLLoader.js";
import { createAxisOverlay, renderAxisOverlay } from "./axis_overlay.js";

const canvas = document.querySelector("#viewport");
const statusEl = document.querySelector("#status");
const paramsEl = document.querySelector("#params");
const legendEl = document.querySelector("#legend");
const cutawayZEl = document.querySelector("#cutawayZ");
const cutawayValueEl = document.querySelector("#cutawayValue");
const cutawayToggle = document.querySelector("#cutawayToggle");
const cutawaySliderPanel = document.querySelector("#cutawaySliderPanel");
const rebuildBar = document.querySelector("#rebuildBar");
const capturePanel = document.querySelector("#capturePanel");
const annotator = document.querySelector("#annotator");
const drawTool = document.querySelector("#drawTool");
const textTool = document.querySelector("#textTool");
const snapshotDialog = document.querySelector("#snapshotDialog");
const snapshotTitle = document.querySelector("#snapshotTitle");
const snapshotTokenEl = document.querySelector("#snapshotToken");
const copySnapshotButton = document.querySelector("#copySnapshot");
const saveCaptureButton = document.querySelector("#saveCapture");
const exportButton = document.querySelector("#exportButton");
const exportMenu = document.querySelector("#exportMenu");

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setClearColor(0xf4f7f9);
renderer.localClippingEnabled = true;
renderer.autoClear = false;

const scene = new THREE.Scene();
scene.add(new THREE.HemisphereLight(0xffffff, 0x334044, 1.7));
const key = new THREE.DirectionalLight(0xffffff, 2.6);
key.position.set(60, -80, 90);
scene.add(key);
const fill = new THREE.DirectionalLight(0xbfd7ff, 0.9);
fill.position.set(-70, 70, 55);
scene.add(fill);

const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 5000);
camera.up.set(0, 0, 1);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.screenSpacePanning = false;
controls.target.set(0, 0, 0);
window.__vibecadRuntime = {
  camera: () => vector(camera.position),
  target: () => vector(controls.target),
};
const axisOverlay = createAxisOverlay();

const grid = new THREE.GridHelper(140, 28, 0x93a6b0, 0xd0dbe1);
grid.rotation.x = Math.PI / 2;
grid.position.z = -0.02;
scene.add(grid);

const partGroup = new THREE.Group();
scene.add(partGroup);

const stlLoader = new STLLoader();
let model = null;
let currentParams = {};
let currentExportUrls = {};
let previewTransforms = {};
let previewOnlyParams = new Set();
let lastMtime = 0;
let lastSignature = "";
let buildSerial = 0;
let isLoading = false;
let saveTimer = null;
let pendingSaveReload = false;
let pendingSaveProgress = false;
let modelBounds = new THREE.Box3();
let modelCenter = new THREE.Vector3();
let clippingPlane = new THREE.Plane(new THREE.Vector3(0, 0, -1), 0);
let cutawayEnabled = false;
let captureTool = "draw";
let textEditor = null;
let savedCaptureToken = "";
let captureUndoStack = [];
const captureToRestore = new URLSearchParams(window.location.search).get("capture");
let restoredCapture = false;

document.querySelector("#refreshButton").addEventListener("click", () => loadModel(true));
document.querySelector("#exportStl").addEventListener("click", () => downloadExport("stl"));
document.querySelector("#exportStep").addEventListener("click", () => downloadExport("step"));
document.querySelector("#captureButton").addEventListener("click", beginCapture);
document.querySelector("#cancelCapture").addEventListener("click", endCapture);
saveCaptureButton.addEventListener("click", saveCapture);
drawTool.addEventListener("click", () => setCaptureTool("draw"));
textTool.addEventListener("click", () => setCaptureTool("text"));
copySnapshotButton.addEventListener("click", copySavedSnapshot);
cutawayZEl.addEventListener("input", updateCutaway);
cutawayToggle.addEventListener("click", () => {
  setCutawayEnabled(!cutawayEnabled);
});
exportButton.addEventListener("click", () => {
  const menu = exportButton.closest(".menu");
  const open = !menu.classList.contains("open");
  menu.classList.toggle("open", open);
  exportButton.setAttribute("aria-expanded", String(open));
});
document.addEventListener("click", (event) => {
  const menu = exportButton.closest(".menu");
  if (!menu.contains(event.target)) {
    menu.classList.remove("open");
    exportButton.setAttribute("aria-expanded", "false");
  }
});
document.addEventListener("keydown", (event) => {
  if (!capturePanel.classList.contains("active")) return;
  if (!(event.key.toLowerCase() === "z" && (event.ctrlKey || event.metaKey) && !event.shiftKey)) return;
  if (textEditor?.input === document.activeElement) return;
  event.preventDefault();
  undoCaptureAnnotation();
});

new ResizeObserver(resize).observe(canvas.parentElement);
resize();
loadModel(true, true);
requestAnimationFrame(tick);
setInterval(() => {
  if (!document.hidden && !isLoading) loadModel(false);
}, 2500);

async function loadModel(forceFit, showProgress = false) {
  const serial = ++buildSerial;
  isLoading = true;
  const showRebuild = showProgress || forceFit || !model;
  if (showRebuild) {
    setRebuilding(true);
    statusEl.textContent = "Rebuilding...";
  }
  try {
    const response = await fetch("/api/model", { cache: "no-store" });
    if (!response.ok) throw new Error((await response.json()).detail || response.statusText);
    const next = await response.json();
    if (serial !== buildSerial) return;
    const signature = modelSignature(next);
    if (!forceFit && signature === lastSignature) {
      return;
    }
    const shouldFitCamera = !model;
    model = next;
    currentParams = next.params;
    currentExportUrls = next.exports;
    previewTransforms = next.previewTransforms || {};
    previewOnlyParams = new Set(next.previewOnlyParams || []);
    renderParams(next.params);
    renderLegend(next.parts);
    await renderParts(next.parts, shouldFitCamera);
    if (captureToRestore && !restoredCapture) {
      await restoreCapture(captureToRestore);
      restoredCapture = true;
    }
    lastMtime = next.modelMtime;
    lastSignature = signature;
    statusEl.textContent = `Ready: ${next.parts.length} parts`;
  } catch (error) {
    statusEl.textContent = `Build failed: ${error.message}`;
  } finally {
    isLoading = false;
    if (showRebuild) {
      setRebuilding(false);
    }
  }
}

async function restoreCapture(captureId) {
  const response = await fetch(`/api/captures/${encodeURIComponent(captureId)}`);
  if (!response.ok) return;
  const metadata = await response.json();
  if (metadata.camera) {
    if (metadata.camera.position) {
      camera.position.set(metadata.camera.position.x, metadata.camera.position.y, metadata.camera.position.z);
    }
    if (metadata.camera.target) {
      controls.target.set(metadata.camera.target.x, metadata.camera.target.y, metadata.camera.target.z);
    }
    if (metadata.camera.up) {
      camera.up.set(metadata.camera.up.x, metadata.camera.up.y, metadata.camera.up.z);
    }
    camera.fov = metadata.camera.fov || camera.fov;
    camera.zoom = metadata.camera.zoom || camera.zoom;
    camera.updateProjectionMatrix();
    controls.update();
  }
  if (metadata.cutaway) {
    setCutawayEnabled(Boolean(metadata.cutaway.enabled));
    if (metadata.cutaway.normalized != null) {
      cutawayZEl.value = metadata.cutaway.normalized;
    } else if (metadata.cutaway.z != null && !modelBounds.isEmpty()) {
      const height = Math.max(modelBounds.max.z - modelBounds.min.z, 0.001);
      cutawayZEl.value = THREE.MathUtils.clamp((metadata.cutaway.z - modelBounds.min.z) / height, 0, 1);
    }
    updateCutaway();
  }
}

async function renderParts(parts, fit) {
  for (const child of [...partGroup.children]) {
    child.geometry?.dispose();
    child.material?.dispose();
    partGroup.remove(child);
  }
  const meshes = await Promise.all(parts.map(loadPart));
  for (const mesh of meshes) partGroup.add(mesh);
  applyPreviewTransforms(previewTransforms);
  modelBounds = new THREE.Box3().setFromObject(partGroup);
  modelCenter = modelBounds.getCenter(new THREE.Vector3());
  updateCutaway();
  if (fit) fitCamera();
}

function loadPart(part) {
  return new Promise((resolve, reject) => {
    stlLoader.load(
      part.stlUrl,
      (geometry) => {
        geometry.computeVertexNormals();
        const color = new THREE.Color(part.color[0], part.color[1], part.color[2]);
        const material = new THREE.MeshStandardMaterial({
          color,
          metalness: 0.05,
          roughness: 0.62,
          clippingPlanes: [],
          clipShadows: true,
        });
        const mesh = new THREE.Mesh(geometry, material);
        mesh.name = part.name;
        resolve(mesh);
      },
      undefined,
      reject,
    );
  });
}

function renderParams(params) {
  paramsEl.replaceChildren();
  for (const [name, spec] of Object.entries(params)) {
    if (isToggleParam(spec)) {
      renderToggleParam(name, spec);
      continue;
    }
    const row = document.createElement("section");
    row.className = "param";
    row.innerHTML = `
      <div class="paramLabel">
        <span>${escapeHtml(spec.label || name)}</span>
        <span class="paramValueWrap">
          <button class="paramValue" data-value type="button" title="Type a value">${formatNumber(spec.value)}</button>
          <button class="paramEdit" data-edit-limits type="button" title="Edit limits" aria-expanded="false">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M12 20h9"></path>
              <path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"></path>
            </svg>
          </button>
        </span>
      </div>
      <input data-slider type="range" min="${spec.min}" max="${spec.max}" step="${spec.step}" value="${spec.value}" />
      <div class="limits" hidden>
        <label>min<input data-field="min" type="number" step="${spec.step}" value="${spec.min}" /></label>
        <label>max<input data-field="max" type="number" step="${spec.step}" value="${spec.max}" /></label>
        <label>step<input data-field="step" type="number" step="0.01" value="${spec.step}" /></label>
      </div>
    `;
    const slider = row.querySelector("[data-slider]");
    const valueEl = row.querySelector("[data-value]");
    const limits = row.querySelector(".limits");
    const editLimits = row.querySelector("[data-edit-limits]");
    slider.addEventListener("input", () => {
      setParamValue(name, Number(slider.value), slider, valueEl, paramSaveOptions(name));
    });
    valueEl.addEventListener("click", () => editParamValue(name, slider, valueEl));
    editLimits.addEventListener("click", () => {
      const open = limits.hidden;
      limits.hidden = !open;
      editLimits.setAttribute("aria-expanded", String(open));
    });
    for (const input of row.querySelectorAll("[data-field]")) {
      input.addEventListener("change", () => {
        const field = input.dataset.field;
        currentParams[name][field] = Number(input.value);
        slider.setAttribute(field, input.value);
        if (field === "step") {
          row.querySelectorAll("[data-field='min'], [data-field='max']").forEach((limitInput) => {
            limitInput.step = input.value;
          });
        }
        setParamValue(name, Number(slider.value), slider, row.querySelector("[data-value]"), paramSaveOptions(name));
      });
    }
    paramsEl.append(row);
  }
}

function renderToggleParam(name, spec) {
  const row = document.createElement("section");
  row.className = "param toggleParam";
  row.innerHTML = `
    <label class="toggleLabel">
      <span>${escapeHtml(spec.label || name)}</span>
      <input data-toggle type="checkbox" ${Number(spec.value) >= 0.5 ? "checked" : ""} />
    </label>
  `;
  const toggle = row.querySelector("[data-toggle]");
  toggle.addEventListener("change", () => {
    const value = toggle.checked ? 1 : 0;
    currentParams[name].value = value;
    scheduleParamSave(paramSaveOptions(name));
  });
  paramsEl.append(row);
}

function isToggleParam(spec) {
  return Number(spec.min) === 0 && Number(spec.max) === 1 && Number(spec.step) === 1;
}

function setParamValue(name, value, slider, valueEl, saveOptions = { reload: true, progress: true }) {
  const nextValue = clampToCurrentLimits(name, value);
  currentParams[name].value = nextValue;
  slider.value = nextValue;
  valueEl.textContent = formatNumber(nextValue);
  if (previewOnlyParams.has(name)) {
    updatePreviewTransforms();
  }
  scheduleParamSave(saveOptions);
}

function editParamValue(name, slider, valueEl) {
  const input = document.createElement("input");
  input.className = "paramValueInput";
  input.type = "number";
  input.min = currentParams[name].min;
  input.max = currentParams[name].max;
  input.step = currentParams[name].step;
  input.value = currentParams[name].value;
  valueEl.replaceWith(input);
  input.focus();
  input.select();
  let done = false;

  const restoreButton = (value) => {
    done = true;
    const valueButton = document.createElement("button");
    valueButton.className = "paramValue";
    valueButton.dataset.value = "";
    valueButton.type = "button";
    valueButton.title = "Type a value";
    valueButton.textContent = formatNumber(value);
    valueButton.addEventListener("click", () => editParamValue(name, slider, valueButton));
    input.replaceWith(valueButton);
    return valueButton;
  };

  const commit = () => {
    if (done) return;
    const nextValue = Number.isFinite(input.valueAsNumber) ? input.valueAsNumber : currentParams[name].value;
    const valueButton = restoreButton(clampToCurrentLimits(name, nextValue));
    setParamValue(name, nextValue, slider, valueButton, paramSaveOptions(name));
  };

  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      commit();
    } else if (event.key === "Escape") {
      restoreButton(currentParams[name].value);
    }
  });
  input.addEventListener("blur", commit);
}

function clampToCurrentLimits(name, value) {
  const spec = currentParams[name];
  return THREE.MathUtils.clamp(value, Number(spec.min), Number(spec.max));
}

async function updatePreviewTransforms() {
  const response = await fetch("/api/preview", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ params: currentParams }),
  });
  if (!response.ok) return;
  const payload = await response.json();
  previewTransforms = payload.previewTransforms || {};
  previewOnlyParams = new Set(payload.previewOnlyParams || [...previewOnlyParams]);
  applyPreviewTransforms(previewTransforms);
}

function applyPreviewTransforms(transforms) {
  const debug = {};
  for (const mesh of partGroup.children) {
    const matrixValues = transforms?.[mesh.name];
    mesh.matrixAutoUpdate = false;
    if (Array.isArray(matrixValues) && matrixValues.length === 16) {
      mesh.matrix.set(...matrixValues);
      debug[mesh.name] = matrixValues;
    } else {
      mesh.matrix.identity();
    }
    mesh.matrixWorldNeedsUpdate = true;
  }
  if (partGroup.children.length > 0) {
    partGroup.updateMatrixWorld(true);
    modelBounds = new THREE.Box3().setFromObject(partGroup);
    modelCenter = modelBounds.getCenter(new THREE.Vector3());
    updateCutaway();
  }
  window.__vibecadPreviewDebug = debug;
}

function paramSaveOptions(name) {
  return previewOnlyParams.has(name) ? { reload: false, progress: false } : { reload: true, progress: true };
}

function renderLegend(parts) {
  legendEl.replaceChildren();
  for (const part of parts) {
    const item = document.createElement("div");
    item.className = "legendItem";
    const color = `rgb(${part.color.map((value) => Math.round(value * 255)).join(" ")})`;
    item.innerHTML = `<span class="swatch" style="background:${color}"></span><span>${escapeHtml(part.name)}</span>`;
    legendEl.append(item);
  }
}

function scheduleParamSave(options = { reload: true, progress: true }) {
  pendingSaveReload = pendingSaveReload || options.reload;
  pendingSaveProgress = pendingSaveProgress || options.progress;
  clearTimeout(saveTimer);
  saveTimer = setTimeout(async () => {
    if (pendingSaveProgress) {
      setRebuilding(true);
    }
    await fetch("/api/params", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ params: currentParams }),
    });
    const shouldReload = pendingSaveReload;
    const shouldShowProgress = pendingSaveProgress;
    pendingSaveReload = false;
    pendingSaveProgress = false;
    if (shouldReload) {
      await loadModel(false, shouldShowProgress);
    } else {
      setRebuilding(false);
    }
  }, 250);
}

function updateCutaway() {
  const normalized = Number(cutawayZEl.value);
  cutawayValueEl.textContent = normalized.toFixed(2);
  const z = cutawayZFromNormalized(normalized);
  const enabled = cutawayEnabled && normalized < 0.999;
  clippingPlane = new THREE.Plane(new THREE.Vector3(0, 0, -1), z);
  for (const mesh of partGroup.children) {
    mesh.material.clippingPlanes = enabled ? [clippingPlane] : [];
    mesh.material.needsUpdate = true;
  }
}

function setCutawayEnabled(enabled) {
  cutawayEnabled = enabled;
  cutawayToggle.setAttribute("aria-pressed", String(enabled));
  cutawayToggle.setAttribute("aria-expanded", String(enabled));
  cutawaySliderPanel.hidden = !enabled;
  updateCutaway();
}

function fitCamera() {
  const box = modelBounds.isEmpty() ? new THREE.Box3().setFromObject(partGroup) : modelBounds;
  if (box.isEmpty()) return;
  const size = box.getSize(new THREE.Vector3());
  const sphere = box.getBoundingSphere(new THREE.Sphere());
  const center = sphere.center.clone();
  modelCenter.copy(center);
  const verticalFov = THREE.MathUtils.degToRad(camera.fov);
  const horizontalFov = 2 * Math.atan(Math.tan(verticalFov / 2) * Math.max(camera.aspect, 0.001));
  const fitDistance = sphere.radius / Math.sin(Math.min(verticalFov, horizontalFov) / 2);
  const distance = Math.max(fitDistance * 0.9, sphere.radius * 1.05, 0.001);
  const direction = new THREE.Vector3(0.72, -0.92, 0.58).normalize();
  controls.target.copy(center);
  camera.position.copy(center).add(direction.multiplyScalar(distance));
  const sceneScale = Math.max(size.x, size.y, size.z, sphere.radius, 0.001);
  camera.near = Math.max(sceneScale / 1000, 0.001);
  camera.far = Math.max(distance + sceneScale * 8, sceneScale * 16);
  camera.lookAt(center);
  camera.updateProjectionMatrix();
  controls.update();
  controls.saveState();
  window.__vibecadDebug = {
    target: vector(controls.target),
    camera: vector(camera.position),
    box: {
      min: vector(box.min),
      max: vector(box.max),
      center: vector(center),
      radius: sphere.radius,
    },
  };
}

function resize() {
  const rect = canvas.parentElement.getBoundingClientRect();
  const width = Math.max(1, Math.floor(rect.width));
  const height = Math.max(1, Math.floor(rect.height));
  renderer.setSize(width, height, false);
  renderer.setViewport(0, 0, width, height);
  renderer.setScissor(0, 0, width, height);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  if (!modelBounds.isEmpty()) {
    fitCamera();
  }
}

function tick() {
  controls.update();
  const size = renderer.getSize(new THREE.Vector2());
  renderer.setViewport(0, 0, size.x, size.y);
  renderer.setScissor(0, 0, size.x, size.y);
  renderer.clear();
  renderer.render(scene, camera);
  renderAxisOverlay(renderer, axisOverlay, camera, controls.target || modelCenter);
  requestAnimationFrame(tick);
}

function downloadExport(fmt) {
  const url = currentExportUrls[fmt];
  if (!url) return;
  exportButton.closest(".menu").classList.remove("open");
  exportButton.setAttribute("aria-expanded", "false");
  window.location.href = url;
}

function beginCapture() {
  removeTextEditor(false);
  savedCaptureToken = "";
  snapshotTokenEl.value = "";
  snapshotDialog.hidden = true;
  snapshotTitle.textContent = "Done";
  copySnapshotButton.disabled = false;
  copySnapshotButton.textContent = "Copy to clipboard";
  saveCaptureButton.disabled = false;
  saveCaptureButton.textContent = "Done";
  setCaptureTool("draw");
  const rect = canvas.getBoundingClientRect();
  const ratio = Math.min(window.devicePixelRatio, 2);
  annotator.width = Math.floor(rect.width * ratio);
  annotator.height = Math.floor(rect.height * ratio);
  annotator.style.width = `${rect.width}px`;
  annotator.style.height = `${rect.height}px`;
  const ctx = annotator.getContext("2d");
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  ctx.drawImage(canvas, 0, 0, rect.width, rect.height);
  ctx.strokeStyle = "#ffdf5e";
  ctx.lineWidth = 4;
  ctx.lineCap = "round";
  ctx.lineJoin = "round";
  captureUndoStack = [];
  capturePanel.classList.add("active");
  statusEl.textContent = "Annotate the screenshot, then click Done";
  let drawing = false;
  annotator.onpointerdown = (event) => {
    if (captureTool === "text") {
      event.preventDefault();
      const point = pointerPoint(event, annotator);
      openTextEditor(point.x, point.y);
      return;
    }
    drawing = true;
    pushCaptureUndoState();
    annotator.setPointerCapture(event.pointerId);
    const point = pointerPoint(event, annotator);
    ctx.beginPath();
    ctx.moveTo(point.x, point.y);
  };
  annotator.onpointermove = (event) => {
    if (!drawing) return;
    const point = pointerPoint(event, annotator);
    ctx.lineTo(point.x, point.y);
    ctx.stroke();
  };
  annotator.onpointerup = () => {
    drawing = false;
  };
}

function endCapture() {
  removeTextEditor(false);
  snapshotDialog.hidden = true;
  saveCaptureButton.disabled = false;
  saveCaptureButton.textContent = "Done";
  capturePanel.classList.remove("active");
  captureUndoStack = [];
}

async function saveCapture() {
  removeTextEditor(true);
  saveCaptureButton.disabled = true;
  saveCaptureButton.textContent = "Saving...";
  const metadata = currentMetadata();
  try {
    const response = await fetch("/api/captures", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: annotator.toDataURL("image/png"), metadata }),
    });
    if (!response.ok) {
      throw new Error(`Capture save failed: ${response.status}`);
    }
    const result = await response.json();
    savedCaptureToken = result.token;
    snapshotTitle.textContent = "Done";
    snapshotTokenEl.value = savedCaptureToken;
    snapshotDialog.hidden = false;
    copySnapshotButton.disabled = false;
    copySnapshotButton.textContent = "Copy to clipboard";
    statusEl.textContent = `Saved ${result.token}`;
  } catch (error) {
    snapshotTitle.textContent = "Save failed";
    snapshotTokenEl.value = "";
    snapshotDialog.hidden = false;
    copySnapshotButton.disabled = true;
    copySnapshotButton.textContent = "Copy unavailable";
    statusEl.textContent = error instanceof Error ? error.message : "Capture save failed";
  } finally {
    saveCaptureButton.disabled = false;
    saveCaptureButton.textContent = "Done";
  }
}

function setCaptureTool(tool) {
  captureTool = tool;
  capturePanel.classList.toggle("textMode", tool === "text");
  drawTool.classList.toggle("active", tool === "draw");
  textTool.classList.toggle("active", tool === "text");
  drawTool.setAttribute("aria-pressed", String(tool === "draw"));
  textTool.setAttribute("aria-pressed", String(tool === "text"));
  if (tool !== "text") removeTextEditor(true);
}

function openTextEditor(x, y) {
  removeTextEditor(true);
  const input = document.createElement("input");
  input.type = "text";
  input.className = "textEditor";
  input.placeholder = "Text";
  input.style.left = `${Math.max(8, x)}px`;
  input.style.top = `${Math.max(8, y)}px`;
  capturePanel.append(input);
  textEditor = { input, x, y };
  input.focus();
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      removeTextEditor(true);
    } else if (event.key === "Escape") {
      event.preventDefault();
      removeTextEditor(false);
    }
  });
  input.addEventListener("blur", () => removeTextEditor(true));
}

function removeTextEditor(commit) {
  if (!textEditor) return;
  const { input, x, y } = textEditor;
  textEditor = null;
  const text = input.value.trim();
  input.remove();
  if (commit && text) {
    pushCaptureUndoState();
    drawTextAnnotation(text, x, y);
  }
}

function drawTextAnnotation(text, x, y) {
  const ctx = annotator.getContext("2d");
  const rect = annotator.getBoundingClientRect();
  const paddingX = 7;
  const paddingY = 5;
  const maxWidth = Math.max(120, rect.width - x - 20);
  ctx.save();
  ctx.font = "15px system-ui, sans-serif";
  ctx.textBaseline = "top";
  const trimmed = text.slice(0, 120);
  const measured = Math.min(ctx.measureText(trimmed).width, maxWidth);
  const boxWidth = measured + paddingX * 2;
  const boxHeight = 28;
  const boxX = Math.min(Math.max(8, x), rect.width - boxWidth - 8);
  const boxY = Math.min(Math.max(8, y), rect.height - boxHeight - 8);
  ctx.fillStyle = "rgba(255, 255, 255, 0.88)";
  ctx.fillRect(boxX, boxY, boxWidth, boxHeight);
  ctx.strokeStyle = "rgba(23, 32, 39, 0.22)";
  ctx.strokeRect(boxX, boxY, boxWidth, boxHeight);
  ctx.fillStyle = "#172027";
  ctx.fillText(trimmed, boxX + paddingX, boxY + paddingY, maxWidth);
  ctx.restore();
}

function pushCaptureUndoState() {
  const ctx = annotator.getContext("2d");
  captureUndoStack.push(ctx.getImageData(0, 0, annotator.width, annotator.height));
  if (captureUndoStack.length > 50) captureUndoStack.shift();
}

function undoCaptureAnnotation() {
  removeTextEditor(false);
  const snapshot = captureUndoStack.pop();
  if (!snapshot) return;
  const ctx = annotator.getContext("2d");
  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.putImageData(snapshot, 0, 0);
  ctx.restore();
}

async function copySavedSnapshot() {
  if (!savedCaptureToken) return;
  snapshotTokenEl.focus();
  snapshotTokenEl.select();
  snapshotTokenEl.setSelectionRange(0, snapshotTokenEl.value.length);
  const copied = await copyTextToClipboard(savedCaptureToken, snapshotTokenEl);
  if (!copied) {
    copySnapshotButton.textContent = "Copy failed";
    statusEl.textContent = "Clipboard write failed";
    return;
  }
  copySnapshotButton.textContent = "Copied to clipboard";
  statusEl.textContent = `Copied ${savedCaptureToken}`;
  window.setTimeout(endCapture, 650);
}

async function copyTextToClipboard(text, sourceInput = null) {
  try {
    const response = await fetch("/api/clipboard", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    if (response.ok) return true;
  } catch {
    // Fall through to browser clipboard fallbacks.
  }
  let copied = false;
  if (sourceInput) {
    try {
      copied = document.execCommand("copy");
    } catch {
      copied = false;
    }
    if (copied) return true;
  }
  if (navigator.clipboard?.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      // Fall through to the selection-based copy path below.
    }
  }
  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.left = "-9999px";
  textarea.style.top = "0";
  document.body.append(textarea);
  textarea.focus();
  textarea.select();
  try {
    copied = document.execCommand("copy");
  } finally {
    textarea.remove();
  }
  return copied;
}

function currentMetadata() {
  return {
    camera: {
      position: vector(camera.position),
      target: vector(controls.target),
      up: vector(camera.up),
      fov: camera.fov,
      zoom: camera.zoom,
    },
    cutaway: {
      enabled: cutawayEnabled,
      normalized: Number(cutawayZEl.value),
      z: cutawayZFromNormalized(Number(cutawayZEl.value)),
    },
    params: Object.fromEntries(Object.entries(currentParams).map(([name, spec]) => [name, spec.value])),
    parts: model?.parts || [],
  };
}

function pointerPoint(event, element) {
  const rect = element.getBoundingClientRect();
  return { x: event.clientX - rect.left, y: event.clientY - rect.top };
}

function vector(v) {
  return { x: v.x, y: v.y, z: v.z };
}

function cutawayZFromNormalized(normalized) {
  if (modelBounds.isEmpty()) return 0;
  return modelBounds.min.z + normalized * (modelBounds.max.z - modelBounds.min.z);
}

function modelSignature(next) {
  const previewOnly = new Set(next.previewOnlyParams || []);
  return JSON.stringify({
    mtime: next.modelMtime,
    parts: next.parts.map((part) => part.cacheKey),
    params: Object.fromEntries(Object.entries(next.params).filter(([name]) => !previewOnly.has(name)).map(([name, spec]) => [name, spec.value])),
  });
}

function setRebuilding(rebuilding) {
  rebuildBar.hidden = !rebuilding;
  rebuildBar.setAttribute("aria-hidden", String(!rebuilding));
}

function formatNumber(value) {
  return Number(value).toLocaleString(undefined, { maximumFractionDigits: 3 });
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" })[char]);
}
