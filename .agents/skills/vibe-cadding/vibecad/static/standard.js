import * as THREE from "three";
import { STLLoader } from "three/addons/loaders/STLLoader.js";
import { createAxisOverlay, renderAxisOverlay } from "./axis_overlay.js";

const loader = new STLLoader();
const views = [...document.querySelectorAll("[data-view]")];

init();

async function init() {
  const response = await fetch("/api/model", { cache: "no-store" });
  if (!response.ok) throw new Error(await response.text());
  const model = await response.json();
  await Promise.all(views.map((canvas) => renderView(canvas, model.parts, model.previewTransforms || {})));
  window.__vibecadReady = true;
}

async function renderView(canvas, parts, previewTransforms) {
  const parent = canvas.parentElement;
  const width = parent.clientWidth;
  const height = parent.clientHeight;
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(width, height, false);
  renderer.setClearColor(0xf4f7f9);
  renderer.autoClear = false;

  const scene = new THREE.Scene();
  scene.add(new THREE.HemisphereLight(0xffffff, 0x334044, 1.7));
  const light = new THREE.DirectionalLight(0xffffff, 2.8);
  light.position.set(60, -80, 90);
  scene.add(light);

  const group = new THREE.Group();
  scene.add(group);
  const meshes = await Promise.all(parts.map(loadPart));
  for (const mesh of meshes) group.add(mesh);
  applyPreviewTransforms(group, previewTransforms);

  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, -5000, 5000);
  camera.up.set(0, 0, 1);
  const target = frameCamera(camera, group, canvas.dataset.view, width / height);
  const axisOverlay = createAxisOverlay(112, 12);
  renderer.clear();
  renderer.render(scene, camera);
  renderAxisOverlay(renderer, axisOverlay, camera, target);
}

function loadPart(part) {
  return new Promise((resolve, reject) => {
    loader.load(
      part.stlUrl,
      (geometry) => {
        geometry.computeVertexNormals();
        const material = new THREE.MeshStandardMaterial({
          color: new THREE.Color(part.color[0], part.color[1], part.color[2]),
          roughness: 0.62,
          metalness: 0.05,
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

function applyPreviewTransforms(group, transforms) {
  for (const mesh of group.children) {
    const matrixValues = transforms?.[mesh.name];
    mesh.matrixAutoUpdate = false;
    if (Array.isArray(matrixValues) && matrixValues.length === 16) {
      mesh.matrix.set(...matrixValues);
    } else {
      mesh.matrix.identity();
    }
    mesh.matrixWorldNeedsUpdate = true;
  }
  group.updateMatrixWorld(true);
}

function frameCamera(camera, object, view, aspect) {
  const box = new THREE.Box3().setFromObject(object);
  const center = box.getCenter(new THREE.Vector3());
  const size = box.getSize(new THREE.Vector3());
  const span = Math.max(size.x, size.y, size.z, 1) * 0.68;
  camera.left = -span * aspect;
  camera.right = span * aspect;
  camera.top = span;
  camera.bottom = -span;

  if (view === "top") {
    camera.position.set(center.x, center.y, center.z + 200);
    camera.up.set(0, 1, 0);
  } else if (view === "front") {
    camera.position.set(center.x, center.y - 200, center.z);
    camera.up.set(0, 0, 1);
  } else if (view === "left") {
    camera.position.set(center.x - 200, center.y, center.z);
    camera.up.set(0, 0, 1);
  } else {
    camera.position.set(center.x + 160, center.y - 180, center.z + 140);
    camera.up.set(0, 0, 1);
  }
  camera.lookAt(center);
  camera.updateProjectionMatrix();
  return center;
}
