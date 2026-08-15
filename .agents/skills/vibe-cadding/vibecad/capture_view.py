from __future__ import annotations

import argparse
import os
import pathlib
from urllib.parse import quote

import httpx


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a vibe-cadding view from the already running server.")
    parser.add_argument("--server", default=os.environ.get("VIBECAD_SERVER", "http://127.0.0.1:8000"))
    parser.add_argument("--out", required=True)
    parser.add_argument("--capture-id", help="Render from a saved screencap camera instead of the standard 2x2 view.")
    parser.add_argument("--width", type=int, default=1400)
    parser.add_argument("--height", type=int, default=1000)
    args = parser.parse_args()

    out = pathlib.Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    if args.capture_id:
        import asyncio

        asyncio.run(_render_capture(args.server.rstrip("/"), args.capture_id, out, args.width, args.height))
        print(out)
    else:
        response = httpx.get(f"{args.server.rstrip('/')}/api/standard-view", timeout=120)
        response.raise_for_status()
        out.write_bytes(response.content)
        print(out)


async def _render_capture(server: str, capture_id: str, out: pathlib.Path, width: int, height: int) -> None:
    from playwright.async_api import async_playwright

    url = f"{server}/?capture={quote(capture_id)}"
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_selector("#status", state="visible")
        await page.wait_for_function("document.querySelector('#status').textContent.startsWith('Ready')", timeout=60000)
        await page.locator(".viewer").screenshot(path=str(out))
        await browser.close()


if __name__ == "__main__":
    main()
