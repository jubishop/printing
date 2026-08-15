import * as THREE from "three";

const AXIS_LENGTH = 1.28;
const AXIS_COLORS = {
  X: 0xff4d4d,
  Y: 0x4fd36b,
  Z: 0x4da3ff,
};

export function createAxisOverlay(size = 124, padding = 14) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 20);
  const group = new THREE.Group();
  scene.add(group);
  scene.add(new THREE.AmbientLight(0xffffff, 2.4));

  addAxis(group, "X", new THREE.Vector3(1, 0, 0));
  addAxis(group, "Y", new THREE.Vector3(0, 1, 0));
  addAxis(group, "Z", new THREE.Vector3(0, 0, 1));

  return { scene, camera, size, padding };
}

export function renderAxisOverlay(renderer, overlay, sourceCamera, target = new THREE.Vector3()) {
  const { scene, camera, size, padding } = overlay;
  const view = renderer.getSize(new THREE.Vector2());
  const axisSize = Math.min(size, view.x * 0.18, view.y * 0.18);
  if (axisSize < 48) return;

  const direction = sourceCamera.position.clone().sub(target);
  if (direction.lengthSq() < 0.001) {
    direction.set(3, -4, 3);
  }
  direction.normalize();

  camera.position.copy(direction.multiplyScalar(3.7));
  camera.up.copy(sourceCamera.up);
  camera.lookAt(0, 0, 0);

  renderer.clearDepth();
  renderer.setScissorTest(true);
  renderer.setViewport(padding, padding, axisSize, axisSize);
  renderer.setScissor(padding, padding, axisSize, axisSize);
  renderer.render(scene, camera);
  renderer.setScissorTest(false);
  renderer.setViewport(0, 0, view.x, view.y);
  renderer.setScissor(0, 0, view.x, view.y);
}

function addAxis(group, label, direction) {
  const color = AXIS_COLORS[label];
  const material = new THREE.MeshBasicMaterial({ color });
  const shaftGeometry = new THREE.CylinderGeometry(0.035, 0.035, AXIS_LENGTH * 0.75, 16);
  const headGeometry = new THREE.ConeGeometry(0.115, 0.28, 24);

  const shaft = new THREE.Mesh(shaftGeometry, material);
  shaft.position.copy(direction.clone().multiplyScalar(AXIS_LENGTH * 0.375));
  orientAlong(shaft, direction);
  group.add(shaft);

  const head = new THREE.Mesh(headGeometry, material);
  head.position.copy(direction.clone().multiplyScalar(AXIS_LENGTH * 0.72));
  orientAlong(head, direction);
  group.add(head);

  const sprite = makeLabel(label, color);
  sprite.position.copy(direction.clone().multiplyScalar(AXIS_LENGTH * 0.82));
  group.add(sprite);
}

function orientAlong(object, direction) {
  object.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), direction.clone().normalize());
}

function makeLabel(text, color) {
  const canvas = document.createElement("canvas");
  canvas.width = 96;
  canvas.height = 96;
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#ffffff";
  ctx.globalAlpha = 0.78;
  ctx.beginPath();
  ctx.arc(48, 48, 28, 0, Math.PI * 2);
  ctx.fill();
  ctx.globalAlpha = 1;
  ctx.fillStyle = `#${color.toString(16).padStart(6, "0")}`;
  ctx.font = "700 42px system-ui, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(text, 48, 50);

  const texture = new THREE.CanvasTexture(canvas);
  texture.colorSpace = THREE.SRGBColorSpace;
  const material = new THREE.SpriteMaterial({ map: texture, transparent: true, depthTest: false, depthWrite: false });
  const sprite = new THREE.Sprite(material);
  sprite.renderOrder = 10;
  sprite.scale.set(0.55, 0.55, 0.55);
  return sprite;
}
