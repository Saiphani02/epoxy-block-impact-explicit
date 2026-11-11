import json, os
ROOT = r"C:\Users\saiph\Documents\GitHub_Projects\Impact_Panel"
DM = Ansys.Mechanical.DataModel.Enums
ExtAPI.Application.ActiveUnitSystem = MechanicalUnitSystem.StandardNMM
M = ExtAPI.DataModel.Project.Model
out = {"mesh": [M.Mesh.Nodes, M.Mesh.Elements]}
st = Ansys.Mechanical.Graphics.GraphicsImageExportSettings(); st.Width = 1600; st.Height = 1000; st.CurrentGraphicsDisplay = False
for a in M.Analyses:
    tag = "deg0" if "0 deg" in a.Name else "deg45"
    r = {"name": a.Name, "status": str(a.Solution.Status)}
    for c in a.Solution.Children:
        if not hasattr(c, "Maximum"): continue
        try:
            r[c.Name] = {"max_end": c.Maximum.Value, "max_over_time": c.MaximumOfMaximumOverTime.Value, "unit": str(c.Maximum.Unit)}
        except Exception as e:
            try: r[c.Name] = {"max_end": c.Maximum.Value, "unit": str(c.Maximum.Unit), "err": str(e)[:80]}
            except: pass
        c.Activate()
        Graphics.Camera.SetSpecificViewOrientation(DM.ViewOrientationType.Iso); Graphics.Camera.SetFit()
        Graphics.ExportImage(os.path.join(ROOT, "media", "%s_%s.png" % (tag, c.Name.replace(" ", "_"))), DM.GraphicsImageExportFormat.PNG, st)
    out[tag] = r
M.Mesh.Activate(); Graphics.Camera.SetSpecificViewOrientation(DM.ViewOrientationType.Iso); Graphics.Camera.SetFit()
Graphics.ExportImage(os.path.join(ROOT, "media", "mesh.png"), DM.GraphicsImageExportFormat.PNG, st)
f_ = open(os.path.join(ROOT, "results", "results.json"), "w"); f_.write(json.dumps(out, indent=1)); f_.close()
ExtAPI.DataModel.Project.SaveAs(os.path.join(ROOT, "epoxy_block_impact.mechdb"))
json.dumps(out)
