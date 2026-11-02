# SKÅDIS paddle holder — validated X2D project

Open the [configured Studio project](modified/skadis-paddle-holder-one-x2d-pla-support.3mf)
to reuse the single-holder setup. The user confirmed that the print completed
and holds their paddle on 2026-11-02. See the
[print record](../../prints/2026-11-02-skadis-paddle-holder.md) and
[case history](../../memory/cases/2026-11-02-skadis-paddle-holder.md).

## Provenance and license

- Model: `Pingpong paddle holder`
- Creator and original profile author: PingPongMeister
- Source: [MakerWorld model 1741694, profile 1850928](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928)
- Exact source profile: `0.2mm layer, 2 walls, 15% infill`, plate 1
- License: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0
  International](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- License checked: 2026-11-02 in the live MakerWorld UI during preflight;
  both the downloaded source and saved project also embed `BY-NC-SA`.
- Artifact: locally modified print project; model geometry was not edited.
- Application: Bambu Studio 2.8.2.61

The original material remains credited to PingPongMeister. This modified
project and the local contributions to it are distributed under the same
CC BY-NC-SA 4.0 license: attribution, noncommercial use, and share-alike apply.
No endorsement by the original creator is implied.

## Local modifications

- Adapted the project to Bambu Lab X2D with 0.4 mm hardened-steel nozzles,
  standard flow, and Textured PEI Plate.
- Synchronized current materials and assigned white Bambu PLA Pure to the
  object. Preserved all five project filament slots so the support interface
  remains filament 5; slots 2–4 are unused by this plate.
- Enabled automatic tree supports, Tree Hybrid, at a 35-degree threshold.
  Support bodies use the object PLA; interfaces use Bambu Support For PLA/PETG
  through the auxiliary nozzle. Avoid interface filament for support body is
  enabled.
- Accepted Studio's material-pair recommendations: zero top Z distance,
  zero interface spacing, rectilinear interlaced interface, 50 mm/s interface
  speed, 5 mm initial support expansion, 3 mm branch diameter, and 7-degree
  branch diameter angle (`tree_support_branch_diameter_angle`).
- Retained one holder, 0.2 mm layers, 2 walls, 15% grid infill, and automatic
  brim configured at 5 mm. The prime tower is enabled.
- Before committing, removed the embedded `DesignerUserId` and `ProfileUserId`
  account identifiers. Creator attribution and license metadata remain.

## Artifact review

The committed ZIP passed its integrity check; XML/JSON entries parsed and
package relationships resolved. All archive content other than the two
removed metadata fields are unchanged from the saved project used for this
print. Geometry, placement, project settings, and material routing were
preserved. The archive contains no generated G-code, credentials, printer
serial numbers, network addresses, or machine-specific local paths. Gallery
images match the original download; the regenerated plate preview shows the
model, not a private camera photo.

The approximately 809 KiB project is stored directly in Git; Git LFS is not
needed for this small artifact. Its SHA-256 is
`46d2b47c014b6c3f2a29952a5821e5d8611f9c066550cfc9caa96d83f6d0550b`.

## Repeating the print

1. Open the committed 3MF in Studio, retaining its project settings. Verify
   the active X2D, nozzles, Textured PEI plate, and one object on plate 1.
2. Confirm filament 1 is the object/support-body PLA and filament 5 is the
   dedicated support interface. Slice and inspect supports, the first several
   layers, prime tower, and nozzle grouping.
3. Map the PLA to the currently loaded main-nozzle feed and support material
   to the auxiliary feed. The successful run used white PLA from AMS A2 and
   support material from the external spool; recheck the live inventory.
4. Set every available calibration control explicitly to Auto immediately
   before sending. These live send-dialog choices are not guaranteed by
   reopening a saved project. Obtain approval after the completed preflight.

The successful run's slice estimated 1h 33m 52s and 23.74 g total. Reopening
and reslicing with a different Studio version may change those estimates.
