# 其他命令

> 共 109 条。

| 命令 | 语法 |
|------|------|
| `ball-zone.create` | `Ball-Zone Create <RANge>` |
| `brick.assemble` | `BRick Assemble keyword <RAnge>` |
| `brick.assemble.group` | `Group s <slot slot >` |
| `brick.assemble.id` | `Id i` |
| `brick.assemble.origin` | `Origin v` |
| `brick.assemble.size` | `Size ix iy iz (*z*-components are 3D-only)` |
| `brick.delete` | `BRick Delete <Range>` |
| `brick.export` | `BRick Export keyword` |
| `brick.export.filename` | `Filename s` |
| `brick.export.id` | `Id i` |
| `brick.export.skip-errors` | `Skip-Errors` |
| `brick.import` | `BRick Import keyword` |
| `brick.import.filename` | `Filename s` |
| `brick.import.id` | `Id i` |
| `brick.make` | `BRick Make <Id i >` |
| `fish.debug` | `fish debug s keyword` |
| `fish.debug.break` | `Break keyword ...` |
| `fish.debug.break.clear` | `CLear` |
| `fish.debug.break.code` | `COde <i > b` |
| `fish.debug.break.fish` | `Fish b` |
| `fish.debug.break.line` | `Line <i > on/off` |
| `fish.debug.codeinto` | `CODEInto` |
| `fish.debug.codeover` | `CODEOver` |
| `fish.debug.codeto` | `CODETo i` |
| `fish.debug.lineinto` | `LINEInto` |
| `fish.debug.lineover` | `LINEOver` |
| `fish.debug.lineto` | `LINETo i` |
| `fish.debug.list` | `LISt keyword ...` |
| `fish.debug.list.call` | `CAll` |
| `fish.debug.list.code` | `COde <i1 > <i2 >` |
| `fish.debug.list.fish` | `Fish` |
| `fish.debug.list.register` | `Register` |
| `fish.debug.list.source` | `SOurce <i1 > <i2 >` |
| `fish.debug.list.stack` | `STack` |
| `fish.debug.run` | `Run` |
| `measure.create` | `MEAsure CREate keyword` |
| `measure.create.bins` | `Bins i fl fh` |
| `measure.create.id` | `Id i` |
| `measure.create.position` | `Position v` |
| `measure.create.position-x` | `Position-X f` |
| `measure.create.position-y` | `Position-Y f` |
| `measure.create.position-z` | `Position-Z f (3D ONLY)` |
| `measure.create.radius` | `Radius f` |
| `measure.create.tolerance` | `Tolerance f` |
| `measure.delete` | `MEAsure DELete <RAnge>` |
| `measure.dump` | `MEAsure Dump ID i keyword` |
| `measure.dump.file` | `File s` |
| `measure.dump.table` | `Table itab` |
| `measure.history` | `Measure History <ID id > keyword ID id2 or v` |
| `measure.history.coordination` | `Coordination` |
| `measure.history.porosity` | `Porosity` |
| `measure.history.position-x` | `Position-X` |
| `measure.history.position-y` | `Position-Y` |
| `measure.history.position-z` | `Position-Z (3D only)` |
| `measure.history.radius` | `Radius` |
| `measure.history.strainrate-xx` | `STRAINRATE-XX` |
| `measure.history.strainrate-xy` | `STRAINRATE-XY` |
| `measure.history.strainrate-xz` | `STRAINRATE-XZ (3D only)` |
| `measure.history.strainrate-yx` | `STRAINRATE-YX` |
| `measure.history.strainrate-yy` | `STRAINRATE-YY` |
| `measure.history.strainrate-yz` | `STRAINRATE-YZ (3D only)` |
| `measure.history.strainrate-zx` | `STRAINRATE-ZX (3D only)` |
| `measure.history.strainrate-zy` | `STRAINRATE-ZY (3D only)` |
| `measure.history.strainrate-zz` | `STRAINRATE-ZZ (3D only)` |
| `measure.history.stress-xx` | `STRESS-XX` |
| `measure.history.stress-xy` | `STRESS-XY` |
| `measure.history.stress-xz` | `STRESS-XZ (3D only)` |
| `measure.history.stress-yx` | `STRESS-YX` |
| `measure.history.stress-yy` | `STRESS-YY` |
| `measure.history.stress-yz` | `STRESS-YZ (3D only)` |
| `measure.history.stress-zx` | `STRESS-ZX (3D only)` |
| `measure.history.stress-zy` | `STRESS-ZY (3D only)` |
| `measure.history.stress-zz` | `STRESS-ZZ (3D only)` |
| `measure.list` | `MEAsure LISt` |
| `measure.modify` | `MEAsure MODify ID i <keyword >` |
| `measure.modify.bins` | `Bins i fl fh` |
| `measure.modify.position` | `Position v` |
| `measure.modify.radius` | `RADius f` |
| `measure.modify.tolerance` | `Tolerance f` |
| `measure.modify.x` | `X f` |
| `measure.modify.y` | `Y f` |
| `measure.modify.z` | `Z f (3D only)` |
| `wall-structure.compute-stiffness` | `Wall-Structure Compute-Stiffness b` |
| `wall-structure.create` | `Wall-Structure Create ... <RANge>` |
| `wall-structure.create.angle` | `Angle f` |
| `wall-structure.create.group` | `Group s <keyword>` |
| `wall-structure.create.group.remove` | `Remove` |
| `wall-structure.create.group.slot` | `Slot s` |
| `wall-structure.create.name` | `Name s` |
| `wall-structure.create.skip-errors` | `Skip-Errors` |
| `wall-structure.create.starting-shell` | `Starting-Shell i` |
| `wall-structure.full-computation` | `Wall-Structure Full-Computation b` |
| `wall-structure.stiffness-factor` | `Wall-Structure Stiffness-Factor f` |
| `wall-structure.update-tolerance` | `Wall-Structure Update-Tolerance f` |
| `wall-zone.compute-stiffness` | `Wall-Zone Compute-Stiffness b` |
| `wall-zone.create` | `Wall-Zone Create ... <RANge>` |
| `wall-zone.create.angle` | `Angle f` |
| `wall-zone.create.face` | `FAce i <Restrict-To-Face>` |
| `wall-zone.create.fill` | `FIll` |
| `wall-zone.create.group` | `Group s <keyword>` |
| `wall-zone.create.group.remove` | `Remove` |
| `wall-zone.create.group.slot` | `Slot s` |
| `wall-zone.create.internal` | `Internal b` |
| `wall-zone.create.name` | `Name s` |
| `wall-zone.create.skip-errors` | `Skip-Errors` |
| `wall-zone.create.starting-zone` | `Starting-Zone i` |
| `wall-zone.full-computation` | `Wall-Zone Full-Computation b` |
| `wall-zone.stiffness-factor` | `Wall-Zone Stiffness-Factor f` |
| `wall-zone.update-tolerance` | `Wall-Zone Update-Tolerance f` |
