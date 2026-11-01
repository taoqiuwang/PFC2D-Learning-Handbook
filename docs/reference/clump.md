# Clump 命令

> 共 227 条。

| 命令 | 语法 |
|------|------|
| `clump.attribute` | `CLump ATtribute keyword ... <RANge>` |
| `clump.attribute.damp` | `DAmp f` |
| `clump.attribute.density` | `DEnsity f` |
| `clump.attribute.displacement` | `DIsplacement v` |
| `clump.attribute.displacement-x` | `Displacement-X f` |
| `clump.attribute.displacement-y` | `Displacement-Y f` |
| `clump.attribute.displacement-z` | `Displacement-Z f (3D ONLY)` |
| `clump.attribute.euler-x` | `Euler-X f (3D ONLY)` |
| `clump.attribute.euler-y` | `Euler-Y f (3D ONLY)` |
| `clump.attribute.euler-z` | `Euler-Z f (3D ONLY)` |
| `clump.attribute.force-applied` | `Force-Applied v` |
| `clump.attribute.force-contact` | `Force-Contact v` |
| `clump.attribute.force-contact-x` | `Force-Contact-X f` |
| `clump.attribute.force-contact-y` | `Force-Contact-Y f` |
| `clump.attribute.force-contact-z` | `Force-Contact-Z f (3D ONLY)` |
| `clump.attribute.fragment` | `Fragment i` |
| `clump.attribute.moi-11` | `Moi-11 f` |
| `clump.attribute.moi-12` | `Moi-12 f` |
| `clump.attribute.moi-13` | `Moi-13 f` |
| `clump.attribute.moi-22` | `Moi-22 f` |
| `clump.attribute.moi-23` | `Moi-23 f` |
| `clump.attribute.moi-33` | `Moi-33 f` |
| `clump.attribute.moi-principal` | `Moi-Principal fprin11 fprin22 fprin33 (3D ONLY)` |
| `clump.attribute.moment-applied` | `Moment-Applied fx fy fz (y- and z- components are 3D ONLY)` |
| `clump.attribute.moment-applied-x` | `Moment-Applied-X f (3D ONLY)` |
| `clump.attribute.moment-applied-y` | `Moment-Applied-Y f (3D ONLY)` |
| `clump.attribute.moment-applied-z` | `Moment-Applied-Z f (3D ONLY)` |
| `clump.attribute.moment-contact` | `Moment-Contact fx fy fz (y- and z- components are 3D ONLY)` |
| `clump.attribute.moment-contact-x` | `Moment-Contact-X f (3D ONLY)` |
| `clump.attribute.moment-contact-y` | `Moment-Contact-Y f (3D ONLY)` |
| `clump.attribute.moment-contact-z` | `Moment-Contact-Z f (3D ONLY)` |
| `clump.attribute.position` | `Position v` |
| `clump.attribute.position-x` | `Position-X f` |
| `clump.attribute.position-y` | `Position-Y f` |
| `clump.attribute.position-z` | `Position-Z f (3D ONLY)` |
| `clump.attribute.rotation` | `ROtation f (2D ONLY)` |
| `clump.attribute.spin` | `Spin fspinx fspiny fspinz (y- and z- components are 3D ONLY)` |
| `clump.attribute.spin-x` | `Spin-X f (3D ONLY)` |
| `clump.attribute.spin-y` | `Spin-Y f (3D ONLY)` |
| `clump.attribute.spin-z` | `Spin-Z f (3D ONLY)` |
| `clump.attribute.velocity` | `Velocity v` |
| `clump.attribute.velocity-x` | `Velocity-X f` |
| `clump.attribute.velocity-y` | `Velocity-Y f` |
| `clump.attribute.velocity-z` | `Velocity-Z f (3D ONLY)` |
| `clump.attribute.volume` | `VOlume f` |
| `clump.create` | `CLump Create keyword ...` |
| `clump.create.calculate` | `Calculate f` |
| `clump.create.density` | `Density f` |
| `clump.create.group` | `Group s <Slot slot > <Pebble> ...` |
| `clump.create.id` | `ID i` |
| `clump.create.inertia` | `INertia fe11 fe22 fe33 fe12 fe13 fe23 (only 1 component in 2D)` |
| `clump.create.pebbles` | `PEbbles i f v` |
| `clump.create.position` | `POsition v` |
| `clump.create.position-x` | `Position-X f` |
| `clump.create.position-y` | `Position-Y f` |
| `clump.create.position-z` | `Position-Z f (3D ONLY)` |
| `clump.create.volume` | `Volume f` |
| `clump.delete` | `CLump Delete <keyword> <RANge>` |
| `clump.delete.clumps` | `Clumps` |
| `clump.delete.pebbles` | `Pebbles` |
| `clump.distribute` | `CLump Distribute keyword ... <RANge>` |
| `clump.distribute.bin` | `BIn ibin` |
| `clump.distribute.bin.azimuth` | `Azimuth fazlow fazhi` |
| `clump.distribute.bin.density` | `DEnsity fdens` |
| `clump.distribute.bin.elevation` | `Elevation fellow felhi (3D ONLY)` |
| `clump.distribute.bin.fish-distribution` | `Fish-Distribution sfish a1...an` |
| `clump.distribute.bin.gauss` | `GAuss <fcutoff >` |
| `clump.distribute.bin.group` | `GRoup s <Slot slot > <Pebble> ...` |
| `clump.distribute.bin.size` | `Size fsizelow <fsizehi >` |
| `clump.distribute.bin.template` | `TEmplate stname` |
| `clump.distribute.bin.tilt` | `TIlt ftiltlow ftilthi (3D ONLY)` |
| `clump.distribute.bin.volume-fraction` | `Volume-Fraction fvfrac` |
| `clump.distribute.box` | `BOx fxmin fxmax fymin fymax fzmin fzmax (*z*-components are 3D ONLY)` |
| `clump.distribute.diameter` | `DIameter` |
| `clump.distribute.fish-size` | `Fish-Size sfname` |
| `clump.distribute.number-bins` | `Number-Bins inum` |
| `clump.distribute.porosity` | `Porosity fporos` |
| `clump.distribute.resolution` | `Resolution fres` |
| `clump.export` | `CLump EXPort keyword <RANge>` |
| `clump.export.geometry` | `Geometry keyword` |
| `clump.export.geometry.resolution` | `Resolution f` |
| `clump.export.geometry.set` | `SEt s` |
| `clump.export.geometry.split` | `SPlit` |
| `clump.export.geometry.surfaces` | `SUrfaces b` |
| `clump.extra` | `CLump EXTra i a<Pebble> <RANge>` |
| `clump.fix` | `CLump FIx keyword ... <RANge>` |
| `clump.fix.spin` | `Spin` |
| `clump.fix.spin-x` | `Spin-X (3D ONLY)` |
| `clump.fix.spin-y` | `Spin-Y (3D ONLY)` |
| `clump.fix.spin-z` | `Spin-Z (3D ONLY)` |
| `clump.fix.velocity` | `Velocity` |
| `clump.fix.velocity-x` | `Velocity-X` |
| `clump.fix.velocity-y` | `Velocity-Y` |
| `clump.fix.velocity-z` | `Velocity-Z (3D ONLY)` |
| `clump.free` | `CLump FRee keyword ... <RANge>` |
| `clump.free.spin` | `Spin` |
| `clump.free.spin-x` | `Spin-X (3D ONLY)` |
| `clump.free.spin-y` | `Spin-Y (3D ONLY)` |
| `clump.free.spin-z` | `Spin-Z (3D ONLY)` |
| `clump.free.velocity` | `Velocity` |
| `clump.free.velocity-x` | `Velocity-X` |
| `clump.free.velocity-y` | `Velocity-Y` |
| `clump.free.velocity-z` | `Velocity-Z (3D ONLY)` |
| `clump.generate` | `CLump Generate keyword ... <RANge>` |
| `clump.generate.azimuth` | `Azimuth fazlow fazhi` |
| `clump.generate.box` | `Box fxmin fxmax fymin fymax fzmin fzmax (*z*-components are 3D ONLY)` |
| `clump.generate.density` | `DEnsity fdens` |
| `clump.generate.diameter` | `DIameter` |
| `clump.generate.elevation` | `Elevation fellow felhi (3D ONLY)` |
| `clump.generate.fish-distribution` | `Fish-Distribution fdist a1...an` |
| `clump.generate.fish-size` | `Fish-Size fsize` |
| `clump.generate.gauss` | `GAuss <fcutoff >` |
| `clump.generate.group` | `GRoup s <Slot slot > <Pebble> ...` |
| `clump.generate.id` | `Id idlow <idhi >` |
| `clump.generate.number` | `Number inum` |
| `clump.generate.size` | `Size fsizelow <fsizehi >` |
| `clump.generate.templates` | `TEmplates inum stname <f > ...` |
| `clump.generate.tilt` | `TIlt ftiltlow ftilthi (3D ONLY)` |
| `clump.generate.tries` | `TRies itries` |
| `clump.group` | `CLump Group s keyword ... <Pebble> <RANge>` |
| `clump.group.remove` | `Remove` |
| `clump.group.slot` | `Slot s` |
| `clump.history` | `CLump History <Name sid > keyword ID id or Position v` |
| `clump.initialize` | `CLump INitialize keyword ... <RANge>` |
| `clump.list` | `CLump List <keyword> <RANge>` |
| `clump.list.attribute` | `Attribute <keyword>` |
| `clump.list.contact` | `COntact <All>` |
| `clump.list.extra` | `EXtra i <Pebble>` |
| `clump.list.group` | `Group s <Pebble>` |
| `clump.list.property` | `Property <s >` |
| `clump.list.result` | `Result` |
| `clump.list.template` | `Template <Attribute s >` |
| `clump.order` | `CLump Order i (3D ONLY)` |
| `clump.property` | `CLump Property s a<s1 a1...> <RANge>` |
| `clump.replicate` | `CLump REPlicate keyword ...` |
| `clump.replicate.angle` | `ANgle fang` |
| `clump.replicate.axis` | `AXis vaxis` |
| `clump.replicate.density` | `DEnsity fden` |
| `clump.replicate.diameter` | `DIameter fdiam` |
| `clump.replicate.fish-size` | `Fish-Size sfname fval` |
| `clump.replicate.group` | `Group s <Slot slot > <Pebble>` |
| `clump.replicate.id` | `Id id` |
| `clump.replicate.name` | `Name s` |
| `clump.replicate.original-position` | `Original-position` |
| `clump.replicate.position` | `Position vpos` |
| `clump.replicate.position-x` | `Position-X fposx` |
| `clump.replicate.position-y` | `Position-Y fposy` |
| `clump.replicate.position-z` | `Position-Z fposz (3D ONLY)` |
| `clump.replicate.volume` | `Volume fvol` |
| `clump.results` | `CLUmp RESults keyword ...` |
| `clump.results.active` | `ACtive b` |
| `clump.results.add-attribute` | `ADd-Attribute s` |
| `clump.results.remove-attribute` | `Remove-Attribute s` |
| `clump.rotate` | `CLump ROtate keyword ... <RANge>` |
| `clump.rotate.angle` | `ANgle fang` |
| `clump.rotate.axis` | `AXis vaxis` |
| `clump.rotate.point` | `Point vrot` |
| `clump.rotate.update-orientation` | `Update-Orientation b` |
| `clump.scale` | `CLump Scale keyword ... <RANge>` |
| `clump.scale.diameter` | `Diameter fdiam` |
| `clump.scale.fish-size` | `Fish-size sfish fval` |
| `clump.scale.volume` | `Volume fvol` |
| `clump.template` | `CLump TEmplate keyword ...` |
| `clump.template.create` | `Create keyword ...` |
| `clump.template.create.bubblepack` | `Bubblepack keyword ...` |
| `clump.template.create.bubblepack.distance` | `Distance fdistance` |
| `clump.template.create.bubblepack.radfactor` | `RADfactor frad` |
| `clump.template.create.bubblepack.ratio` | `RATio fratio` |
| `clump.template.create.bubblepack.refinenum` | `REfinenum i` |
| `clump.template.create.geometry` | `Geometry s` |
| `clump.template.create.inertia` | `INertia fe11 fe22 fe33 fe12 fe13 fe23 (only 1 component in 2D)` |
| `clump.template.create.name` | `Name s` |
| `clump.template.create.pebbles` | `PEBbles inumber frad vpos` |
| `clump.template.create.pebcalculate` | `PEBCalculate ftol` |
| `clump.template.create.position` | `POsition vcpos` |
| `clump.template.create.position-x` | `Position-X fposx` |
| `clump.template.create.position-y` | `Position-Y fposy` |
| `clump.template.create.position-z` | `Position-Z fposz (3D ONLY)` |
| `clump.template.create.surfcalculate` | `Surfcalculate` |
| `clump.template.create.volume` | `Volume fvol` |
| `clump.template.delete` | `Delete s` |
| `clump.template.delete.name` | `Name s` |
| `clump.template.export` | `Export s <keyword ...>` |
| `clump.template.export.filename` | `Filename s` |
| `clump.template.export.skip-errors` | `Skip-Errors` |
| `clump.template.import` | `Import s keyword ...` |
| `clump.template.import.name` | `Name s` |
| `clump.tolerance` | `CLump TOlerance keyword ...` |
| `clump.tolerance.constant` | `Constant fctol <RANge>` |
| `clump.tolerance.extent` | `Extent fetol` |
| `clump.tolerance.velocity` | `Velocity fvtol` |
| `clump.trace` | `CLump TRace <ID id > <pebble> ID id2 or v` |
| `displacement` | `Displacement` |
| `displacement.displacement-x` | `Displacement-X` |
| `displacement.displacement-y` | `Displacement-Y` |
| `displacement.displacement-z` | `Displacement-Z (3D ONLY)` |
| `displacement.euler-x` | `Euler-X (3D ONLY)` |
| `displacement.euler-y` | `Euler-Y (3D ONLY)` |
| `displacement.euler-z` | `Euler-Z (3D ONLY)` |
| `displacement.force-contact` | `Force-Contact` |
| `displacement.force-contact-x` | `Force-Contact-X` |
| `displacement.force-contact-y` | `Force-Contact-Y` |
| `displacement.force-contact-z` | `Force-Contact-Z (3D ONLY)` |
| `displacement.force-unbalanced` | `Force-Unbalanced` |
| `displacement.force-unbalanced-x` | `Force-Unbalanced-X` |
| `displacement.force-unbalanced-y` | `Force-Unbalanced-Y` |
| `displacement.force-unbalanced-z` | `Force-Unbalanced-Z (3D ONLY)` |
| `displacement.moment-contact` | `Moment-Contact` |
| `displacement.moment-contact-x` | `Moment-Contact-X (3D ONLY)` |
| `displacement.moment-contact-y` | `Moment-Contact-Y (3D ONLY)` |
| `displacement.moment-contact-z` | `Moment-Contact-Z (3D ONLY)` |
| `displacement.moment-unbalanced` | `Moment-Unbalanced` |
| `displacement.moment-unbalanced-x` | `Moment-Unbalanced-X (3D ONLY)` |
| `displacement.moment-unbalanced-y` | `Moment-Unbalanced-Y (3D ONLY)` |
| `displacement.moment-unbalanced-z` | `Moment-Unbalanced-Z (3D ONLY)` |
| `displacement.position-x` | `Position-X` |
| `displacement.position-y` | `Position-Y` |
| `displacement.position-z` | `Position-Z (3D ONLY)` |
| `displacement.rotation` | `ROtation (2D ONLY)` |
| `displacement.spin` | `Spin` |
| `displacement.spin-x` | `Spin-X (3D ONLY)` |
| `displacement.spin-y` | `Spin-Y (3D ONLY)` |
| `displacement.spin-z` | `Spin-Z (3D ONLY)` |
| `displacement.velocity` | `Velocity` |
| `displacement.velocity-x` | `Velocity-X` |
| `displacement.velocity-y` | `Velocity-Y` |
| `displacement.velocity-z` | `Velocity-Z` |
