# Figma REST API reference (what this skill relies on)

Base URL: `https://api.figma.com`
Auth header on every request: `X-Figma-Token: <personal access token>`

Generate a token at **Figma → Settings → Security → Personal access tokens**. The
token needs at least *File content* (read) scope; *Library content* helps if you
pull published styles. Store it in the `FIGMA_TOKEN` env var — never hard-code it.

## Endpoints used

| Purpose | Endpoint | Notes |
| --- | --- | --- |
| Whole file tree | `GET /v1/files/{file_key}` | Big. Use only when you need the full document. |
| Specific node(s) | `GET /v1/files/{file_key}/nodes?ids=1:2,3:4` | Preferred — fetch just the frame you're converting. |
| Render to image | `GET /v1/images/{file_key}?ids=...&format=svg\|png&scale=2` | Returns `{images: {nodeId: url}}`; URLs expire, download promptly. |
| Raster fill refs | `GET /v1/files/{file_key}/images` | Maps `imageRef` → URL for `type: IMAGE` fills. |
| Published styles | `GET /v1/files/{file_key}/styles` | Optional; named color/text styles. |

## URL anatomy

A design URL looks like:
```
https://www.figma.com/design/AbCdEf123/Project?node-id=12-34&t=...
                              ^file_key                ^node-id (12-34 == 12:34)
```
Figma writes node ids as `12-34` in URLs but the API expects `12:34`. The client
(`figma_client.parse_figma_url`) handles the swap.

## Node fields the generator reads

- **Layout**: `layoutMode` (NONE/HORIZONTAL/VERTICAL), `itemSpacing`,
  `paddingTop/Bottom/Left/Right`, `primaryAxisAlignItems`, `counterAxisAlignItems`,
  `layoutSizingHorizontal/Vertical` (FIXED/HUG/FILL).
- **Geometry**: `absoluteBoundingBox` (width/height), `cornerRadius`.
- **Paint**: `fills[]`, `strokes[]`, `strokeWeight`, `opacity` — colors are RGBA
  floats in 0..1, *not* 0..255.
- **Effects**: `effects[]` (DROP_SHADOW with `radius`, `offset`, `color`).
- **Text**: `characters`, `style.fontSize`, `style.fontWeight`,
  `style.textAlignHorizontal`, `style.lineHeightPx`.

## Rate limits & gotchas

- The image endpoint is async-ish: a `url` may be `null` if rendering isn't ready —
  retry after a short delay.
- Rendered image URLs are short-lived S3 links; download immediately.
- Large files: prefer `/nodes?ids=` over the whole-file endpoint to stay fast and
  under rate limits. The client retries 429/5xx with exponential backoff.
