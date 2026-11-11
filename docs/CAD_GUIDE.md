# Epoxy impact CAD and simulation guide

## Download

Use **Code → Download ZIP** on the repository home page and extract the ZIP before opening the files. For one file, open its GitHub page and choose the raw-file download. Keep the original download and edit a working copy.

## File formats

STEP stores exchange geometry; it does not preserve the original sketch constraints or feature history. Native application files are the starting point for inspecting the editable model. Images and videos are previews; numerical tables are documented results.

## Open the model

1. Open a working copy of [epoxy_block_impact.mechdb](../ansys/epoxy_block_impact.mechdb) in ANSYS Mechanical 2026 R1.
2. Inspect geometry references, epoxy material, the fixed bottom face, mesh, and initial velocity.
3. Compare the setup with the [model description](../README.md#model) and [recorded walkthrough](../media/ansys_walkthrough.mp4).
4. Review the 0° and 45° cases before solving. The database's saved state should be checked rather than assumed to contain both configurations ready to run.
5. Compare the output with [results.json](../results/results.json) and the published contour images in [media/](../media/).

The native file is a Mechanical database, not a complete Workbench archive. For CAD geometry alone, import [block_200mm.step](../geometry/block_200mm.step) and confirm the 200 mm dimensions. The repository does not include a native Fusion design file.

## Analysis records

- [Epoxy material data](../ansys/epoxy_material.xml).
- [Mesh preview](../media/mesh.png).
- [0° deformation](../media/deg0_Total_Deformation.png) and [stress](../media/deg0_Equivalent_Stress.png).
- [45° deformation](../media/deg45_Total_Deformation.png) and [stress](../media/deg45_Equivalent_Stress.png).

The README distinguishes peak values across the full run from the final-time contour images.

## Supporting calculations

[export_results.py](../ansys/export_results.py) supports numerical export. [wave_check.py](../hand_check/wave_check.py) supplies analytical estimates. Opening the native model, STEP geometry, screenshots, or video does not require executing these scripts.

## Review status

This documentation update does not constitute a new solve or compatibility test. Retain the original study context and assumptions in the [README](../README.md).
