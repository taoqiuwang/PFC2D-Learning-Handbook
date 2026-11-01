# RBlock 命令

> 共 352 条。

| 命令 | 语法 |
|------|------|
| `rblock.attribute` | `rblock ATtribute keyword ... <RANge>` |
| `rblock.attribute.damp` | `DAmp f` |
| `rblock.attribute.density` | `DEnsity f` |
| `rblock.attribute.displacement` | `DIsplacement v` |
| `rblock.attribute.displacement-x` | `Displacement-X f` |
| `rblock.attribute.displacement-y` | `Displacement-Y f` |
| `rblock.attribute.displacement-z` | `Displacement-Z f (3D ONLY)` |
| `rblock.attribute.euler` | `Euler v (3D ONLY)` |
| `rblock.attribute.euler-x` | `Euler-X f (3D ONLY)` |
| `rblock.attribute.euler-y` | `Euler-Y f (3D ONLY)` |
| `rblock.attribute.euler-z` | `Euler-Z f (3D ONLY)` |
| `rblock.attribute.force-applied` | `Force-Applied v` |
| `rblock.attribute.force-applied-x` | `Force-Applied-X f` |
| `rblock.attribute.force-applied-y` | `Force-Applied-Y f` |
| `rblock.attribute.force-applied-z` | `Force-Applied-Z f (3D ONLY)` |
| `rblock.attribute.force-contact` | `Force-Contact v` |
| `rblock.attribute.force-contact-x` | `Force-Contact-X f` |
| `rblock.attribute.force-contact-y` | `Force-Contact-Y f` |
| `rblock.attribute.force-contact-z` | `Force-Contact-Z f (3D ONLY)` |
| `rblock.attribute.fragment` | `Fragment i` |
| `rblock.attribute.moi-11` | `Moi-11 f` |
| `rblock.attribute.moi-12` | `Moi-12 f` |
| `rblock.attribute.moi-13` | `Moi-13 f` |
| `rblock.attribute.moi-22` | `Moi-22 f` |
| `rblock.attribute.moi-23` | `Moi-23 f` |
| `rblock.attribute.moi-33` | `Moi-33 f` |
| `rblock.attribute.moi-principal` | `Moi-Principal fprin11 fprin22 fprin33 (3D ONLY)` |
| `rblock.attribute.moment-applied` | `Moment-Applied fx fy fz (y- and z- components are 3D ONLY)` |
| `rblock.attribute.moment-applied-x` | `Moment-Applied-X f (3D ONLY)` |
| `rblock.attribute.moment-applied-y` | `Moment-Applied-Y f (3D ONLY)` |
| `rblock.attribute.moment-applied-z` | `Moment-Applied-Z f (3D ONLY)` |
| `rblock.attribute.moment-contact` | `Moment-Contact fx fy fz (y- and z- components are 3D ONLY)` |
| `rblock.attribute.moment-contact-x` | `Moment-Contact-X f (3D ONLY)` |
| `rblock.attribute.moment-contact-y` | `Moment-Contact-Y f (3D ONLY)` |
| `rblock.attribute.moment-contact-z` | `Moment-Contact-Z f (3D ONLY)` |
| `rblock.attribute.position` | `Position v` |
| `rblock.attribute.position-x` | `Position-X f` |
| `rblock.attribute.position-y` | `Position-Y f` |
| `rblock.attribute.position-z` | `Position-Z f (3D ONLY)` |
| `rblock.attribute.rotation` | `ROtation f (2D ONLY)` |
| `rblock.attribute.spin` | `Spin fspinx fspiny fspinz (y- and z- components are 3D ONLY)` |
| `rblock.attribute.spin-x` | `Spin-X f (3D ONLY)` |
| `rblock.attribute.spin-y` | `Spin-Y f (3D ONLY)` |
| `rblock.attribute.spin-z` | `Spin-Z f (3D ONLY)` |
| `rblock.attribute.velocity` | `Velocity v` |
| `rblock.attribute.velocity-x` | `Velocity-X f` |
| `rblock.attribute.velocity-y` | `Velocity-Y f` |
| `rblock.attribute.velocity-z` | `Velocity-Z f (3D ONLY)` |
| `rblock.attribute.volume` | `VOlume f` |
| `rblock.construct` | `rblock Construct keyword ...` |
| `rblock.construct.density` | `Density f` |
| `rblock.construct.from-balls` | `From-Balls <keyword>` |
| `rblock.construct.from-balls.periodicity` | `PEriodicity bx by bz (z-component is 3D ONLY)` |
| `rblock.construct.from-balls.polydisperse` | `POlydisperse b` |
| `rblock.construct.from-geometry` | `From-Geometry <set > keyword ... <RANge>` |
| `rblock.construct.from-geometry.delaunay` | `Delaunay` |
| `rblock.construct.from-geometry.hexahedral` | `Hexahedral (3D ONLY)` |
| `rblock.construct.from-geometry.internal` | `Internal (3D ONLY)` |
| `rblock.construct.from-geometry.maximum-edge` | `Maximum-Edge f` |
| `rblock.construct.from-geometry.minimum-edge` | `Minimum-Edge f` |
| `rblock.construct.from-geometry.patch-angle-tolerance` | `Patch-Angle-Tolerance f` |
| `rblock.construct.from-geometry.quadrilateral` | `Quadrilateral f <All>` |
| `rblock.construct.from-geometry.tetrahedral` | `Tetrahedral (3D ONLY)` |
| `rblock.construct.from-geometry.voronoi` | `Voronoi` |
| `rblock.construct.group` | `Group s <Slot slot > ...` |
| `rblock.construct.rounding` | `Rounding f <Relative>` |
| `rblock.contact-resolution` | `rblock Contact-Resolution keyword ...` |
| `rblock.contact-resolution.full` | `Full` |
| `rblock.contact-resolution.inhibit-contacts` | `Inhibit-Contacts <keyword>` |
| `rblock.contact-resolution.inhibit-contacts.face-maximum` | `Face-Maximum f` |
| `rblock.contact-resolution.inhibit-contacts.face-minimum` | `Face-Minimum f` |
| `rblock.contact-resolution.inhibit-contacts.probability` | `Probability f` |
| `rblock.contact-resolution.inhibit-interval` | `Inhibit-Interval i` |
| `rblock.contact-resolution.reduced` | `Reduced` |
| `rblock.contact-resolution.tolerance` | `Tolerance f` |
| `rblock.contact-resolution.update-area` | `Update-Area b` |
| `rblock.create` | `rblock CReate keyword ...` |
| `rblock.create.box` | `Box fxmin fxmax <fymin fymax <fzmin fzmax >> (z-components are 3D ONLY)` |
| `rblock.create.circle` | `CIrcle keyword ... (2D ONLY)` |
| `rblock.create.circle.position` | `Position vpos` |
| `rblock.create.circle.radius` | `RAdius frad` |
| `rblock.create.circle.resolution` | `Resolution fres` |
| `rblock.create.cone` | `COne keyword ... (3D only)` |
| `rblock.create.cone.axis` | `Axis v3` |
| `rblock.create.cone.base` | `Base v3` |
| `rblock.create.cone.height` | `Height fh` |
| `rblock.create.cone.radius` | `RAdius fbot <ftop >` |
| `rblock.create.cone.resolution` | `REsolution fres` |
| `rblock.create.cylinder` | `CYlinder keyword ... (3D Only)` |
| `rblock.create.cylinder.axis` | `Axis v3` |
| `rblock.create.cylinder.base` | `Base v3` |
| `rblock.create.cylinder.height` | `Height fh` |
| `rblock.create.cylinder.radius` | `RAdius frad` |
| `rblock.create.cylinder.resolution` | `REsolution fres` |
| `rblock.create.density` | `Density f` |
| `rblock.create.from-geometry` | `From-Geometry <set > <RANge>` |
| `rblock.create.group` | `Group s <Slot slot > ...` |
| `rblock.create.id` | `ID i` |
| `rblock.create.rounding` | `Rounding <Relative> f` |
| `rblock.create.sphere` | `Sphere keyword ... (3D ONLY)` |
| `rblock.create.sphere.position` | `Position vpos` |
| `rblock.create.sphere.radius` | `RAdius frad` |
| `rblock.create.sphere.resolution` | `Resolution fres` |
| `rblock.create.vertices` | `Vertices v1 v2 ...` |
| `rblock.cut` | `rblock CUt keyword ... <RANge>` |
| `rblock.cut.aspect-ratio` | `Aspect-Ratio f` |
| `rblock.cut.fractures` | `Fractures <s > <keyword ...>` |
| `rblock.cut.fractures.infinite-plane` | `Infinite-plane` |
| `rblock.cut.fractures.throughgoing` | `Throughgoing` |
| `rblock.cut.group` | `Group s <Slot slot >` |
| `rblock.cut.intersects-box` | `Intersects-Box fxmin fxmax <fymin fymax <fzmin fzmax >> (z-components are 3D ONLY)` |
| `rblock.cut.persistence` | `Persistence f` |
| `rblock.cut.plane` | `Plane keyword ...` |
| `rblock.cut.plane.normal` | `Normal vnorm` |
| `rblock.cut.plane.point` | `Point vpt` |
| `rblock.cut.plane.radius` | `Radius f` |
| `rblock.cut.remove-sliver` | `Remove-Sliver b` |
| `rblock.cut.size` | `Size keyword` |
| `rblock.cut.size.absolute` | `Absolute f` |
| `rblock.cut.size.relative` | `Relative f` |
| `rblock.delete` | `rblock Delete <keyword> <RANge>` |
| `rblock.delete.aspect-ratio` | `Aspect-Ratio f1 <f2 >` |
| `rblock.delete.size` | `Size keyword` |
| `rblock.delete.size.absolute` | `Absolute f1 <f2 >` |
| `rblock.delete.size.ratio-maximum` | `Ratio-Maximum f` |
| `rblock.delete.size.ratio-mean` | `Ratio-Mean f` |
| `rblock.dilate` | `rblock Dilate <keyword> f <keyword> <RANge>` |
| `rblock.dilate.keep-inertial` | `Keep-Inertial` |
| `rblock.dilate.relative` | `Relative` |
| `rblock.distribute` | `rblock Distribute keyword ... <RANge>` |
| `rblock.distribute.bin` | `BIn ibin` |
| `rblock.distribute.bin.azimuth` | `Azimuth fazlow fazhi` |
| `rblock.distribute.bin.density` | `DEnsity fdens` |
| `rblock.distribute.bin.elevation` | `Elevation fellow felhi (3D ONLY)` |
| `rblock.distribute.bin.fish-distribution` | `Fish-Distribution sfish a1...an` |
| `rblock.distribute.bin.gauss` | `GAuss <fcutoff >` |
| `rblock.distribute.bin.group` | `GRoup s <Slot slot >` |
| `rblock.distribute.bin.size` | `Size fsizelow <fsizehi >` |
| `rblock.distribute.bin.template` | `TEmplate stname` |
| `rblock.distribute.bin.tilt` | `TIlt ftiltlow ftilthi (3D ONLY)` |
| `rblock.distribute.bin.volume-fraction` | `Volume-Fraction fvfrac` |
| `rblock.distribute.box` | `BOx fxmin fxmax fymin fymax fzmin fzmax (z-components are 3D ONLY)` |
| `rblock.distribute.diameter` | `DIameter` |
| `rblock.distribute.fish-size` | `Fish-Size sfname` |
| `rblock.distribute.number-bins` | `Number-Bins inum` |
| `rblock.distribute.porosity` | `Porosity fporos` |
| `rblock.distribute.resolution` | `Resolution fres` |
| `rblock.erode` | `rblock Erode <keyword> f <RANge>` |
| `rblock.erode.minimum-distance` | `Minimum-Distance` |
| `rblock.erode.relative` | `Relative` |
| `rblock.erode.skip-errors` | `Skip-Errors` |
| `rblock.export` | `rblock EXPort keyword <RANge>` |
| `rblock.export.to-geometry` | `To-Geometry <s > keyword ...` |
| `rblock.export.to-geometry.slot` | `Slot s` |
| `rblock.export.to-geometry.split` | `Split` |
| `rblock.export.to-geometry.to-3dec5` | `To-3DEC5 s <keyword> (3D ONLY)` |
| `rblock.export.to-geometry.to-3dec5.constitutive` | `Constitutive i` |
| `rblock.export.to-geometry.to-3dec5.group` | `Group s <Slot i >` |
| `rblock.export.to-geometry.to-3dec5.material` | `Material i` |
| `rblock.export.to-geometry.to-3dec5.region` | `Region i` |
| `rblock.extra` | `rblock EXTra i a<RANge>` |
| `rblock.fix` | `rblock FIx keyword ... <RANge>` |
| `rblock.fix.spin` | `Spin` |
| `rblock.fix.spin-x` | `Spin-X (3D ONLY)` |
| `rblock.fix.spin-y` | `Spin-Y (3D ONLY)` |
| `rblock.fix.spin-z` | `Spin-Z (3D ONLY)` |
| `rblock.fix.velocity` | `Velocity` |
| `rblock.fix.velocity-x` | `Velocity-X` |
| `rblock.fix.velocity-y` | `Velocity-Y` |
| `rblock.fix.velocity-z` | `Velocity-Z (3D ONLY)` |
| `rblock.free` | `rblock FRee keyword ... <RANge>` |
| `rblock.free.spin` | `Spin` |
| `rblock.free.spin-x` | `Spin-X (3D ONLY)` |
| `rblock.free.spin-y` | `Spin-Y (3D ONLY)` |
| `rblock.free.spin-z` | `Spin-Z (3D ONLY)` |
| `rblock.free.velocity` | `Velocity` |
| `rblock.free.velocity-x` | `Velocity-X` |
| `rblock.free.velocity-y` | `Velocity-Y` |
| `rblock.free.velocity-z` | `Velocity-Z (3D ONLY)` |
| `rblock.generate` | `rblock Generate keyword ... <RANge>` |
| `rblock.generate.azimuth` | `Azimuth fazlow fazhi` |
| `rblock.generate.box` | `Box fxmin fxmax fymin fymax fzmin fzmax (z-components are 3D ONLY)` |
| `rblock.generate.density` | `DEnsity fdens` |
| `rblock.generate.diameter` | `DIameter` |
| `rblock.generate.elevation` | `Elevation fellow felhi (3D ONLY)` |
| `rblock.generate.fish-distribution` | `Fish-Distribution fdist a1...an` |
| `rblock.generate.fish-size` | `Fish-Size fsize` |
| `rblock.generate.gauss` | `GAuss <fcutoff >` |
| `rblock.generate.group` | `GRoup s <Slot slot > ...` |
| `rblock.generate.id` | `Id idlow <idhi >` |
| `rblock.generate.number` | `Number inum` |
| `rblock.generate.size` | `Size fsizelow <fsizehi >` |
| `rblock.generate.templates` | `TEmplates inum stname <f > ...` |
| `rblock.generate.tilt` | `TIlt ftiltlow ftilthi (3D ONLY)` |
| `rblock.generate.tries` | `TRies itries` |
| `rblock.group` | `rblock Group s keyword ... <RANge>` |
| `rblock.group.add` | `Add` |
| `rblock.group.remove` | `Remove` |
| `rblock.group.slot` | `Slot slot` |
| `rblock.history` | `rblock History <Name sid > keyword ID id or Position v` |
| `rblock.history.displacement` | `Displacement` |
| `rblock.history.displacement-x` | `Displacement-X` |
| `rblock.history.displacement-y` | `Displacement-Y` |
| `rblock.history.displacement-z` | `Displacement-Z (3D ONLY)` |
| `rblock.history.euler-x` | `Euler-X (3D ONLY)` |
| `rblock.history.euler-y` | `Euler-Y (3D ONLY)` |
| `rblock.history.euler-z` | `Euler-Z (3D ONLY)` |
| `rblock.history.force-contact` | `Force-Contact` |
| `rblock.history.force-contact-x` | `Force-Contact-X` |
| `rblock.history.force-contact-y` | `Force-Contact-Y` |
| `rblock.history.force-contact-z` | `Force-Contact-Z (3D ONLY)` |
| `rblock.history.force-unbalanced` | `Force-Unbalanced` |
| `rblock.history.force-unbalanced-x` | `Force-Unbalanced-X` |
| `rblock.history.force-unbalanced-y` | `Force-Unbalanced-Y` |
| `rblock.history.force-unbalanced-z` | `Force-Unbalanced-Z (3D ONLY)` |
| `rblock.history.moment-contact` | `Moment-Contact` |
| `rblock.history.moment-contact-x` | `Moment-Contact-X (3D ONLY)` |
| `rblock.history.moment-contact-y` | `Moment-Contact-Y (3D ONLY)` |
| `rblock.history.moment-contact-z` | `Moment-Contact-Z (3D ONLY)` |
| `rblock.history.moment-unbalanced` | `Moment-Unbalanced` |
| `rblock.history.moment-unbalanced-x` | `Moment-Unbalanced-X (3D ONLY)` |
| `rblock.history.moment-unbalanced-y` | `Moment-Unbalanced-Y (3D ONLY)` |
| `rblock.history.moment-unbalanced-z` | `Moment-Unbalanced-Z (3D ONLY)` |
| `rblock.history.position-x` | `Position-X` |
| `rblock.history.position-y` | `Position-Y` |
| `rblock.history.position-z` | `Position-Z (3D ONLY)` |
| `rblock.history.rotation` | `ROtation (2D ONLY)` |
| `rblock.history.spin` | `Spin` |
| `rblock.history.spin-x` | `Spin-X (3D ONLY)` |
| `rblock.history.spin-y` | `Spin-Y (3D ONLY)` |
| `rblock.history.spin-z` | `Spin-Z (3D ONLY)` |
| `rblock.history.velocity` | `Velocity` |
| `rblock.history.velocity-x` | `Velocity-X` |
| `rblock.history.velocity-y` | `Velocity-Y` |
| `rblock.history.velocity-z` | `Velocity-Z` |
| `rblock.import` | `rblock Import keyword ... <RANge>` |
| `rblock.import.density` | `Density f` |
| `rblock.import.from-geometry` | `From-Geometry <set > keyword ...` |
| `rblock.import.group` | `Group s <Slot slot > ...` |
| `rblock.import.rounding` | `Rounding f <Relative>` |
| `rblock.import.start-set` | `Start-Set s` |
| `rblock.initialize` | `rblock INitialize keyword ... <RANge>` |
| `rblock.list` | `rblock List <keyword> <RANge>` |
| `rblock.list.attribute` | `Attribute <keyword>` |
| `rblock.list.contact` | `COntact <All>` |
| `rblock.list.extra` | `EXtra i` |
| `rblock.list.group` | `Group slot` |
| `rblock.list.property` | `Property <s >` |
| `rblock.list.result` | `Result` |
| `rblock.list.template` | `Template <Attribute s >` |
| `rblock.merge` | `rblock Merge <keyword> <RANge>` |
| `rblock.merge.density` | `Density f` |
| `rblock.merge.group` | `Group s <Slot slot > ...` |
| `rblock.merge.id` | `Id i` |
| `rblock.merge.keep-source` | `Keep-Source` |
| `rblock.merge.rounding` | `Rounding f <Relative>` |
| `rblock.property` | `rblock Property s a<s1 a1...> <RANge>` |
| `rblock.replicate` | `rblock REPlicate s keyword ...` |
| `rblock.replicate.angle` | `ANgle fang` |
| `rblock.replicate.axis` | `AXis vaxis (3D ONLY)` |
| `rblock.replicate.density` | `DEnsity fden` |
| `rblock.replicate.diameter` | `DIameter fdiam` |
| `rblock.replicate.fish-size` | `Fish-Size sfname fval` |
| `rblock.replicate.group` | `Group s <Slot slot >` |
| `rblock.replicate.id` | `Id id` |
| `rblock.replicate.original-position` | `Original-position` |
| `rblock.replicate.position` | `Position vpos` |
| `rblock.replicate.position-x` | `Position-X fposx` |
| `rblock.replicate.position-y` | `Position-Y fposy` |
| `rblock.replicate.position-z` | `Position-Z fposz (3D ONLY)` |
| `rblock.replicate.size` | `Size f` |
| `rblock.results` | `rblock RESults keyword ...` |
| `rblock.results.active` | `ACtive b` |
| `rblock.results.add-attribute` | `ADd-Attribute s` |
| `rblock.results.remove-attribute` | `Remove-Attribute s` |
| `rblock.rotate` | `rblock ROtate keyword ... <RANge>` |
| `rblock.rotate.angle` | `ANgle fang` |
| `rblock.rotate.axis` | `AXis vaxis` |
| `rblock.rotate.point` | `Point vrot` |
| `rblock.rotate.update-orientation` | `Update-Orientation b` |
| `rblock.scale` | `rblock Scale keyword ... <RANge>` |
| `rblock.scale.diameter` | `Diameter fdiam` |
| `rblock.scale.fish-size` | `Fish-Size sfish fval` |
| `rblock.scale.keep-inertial` | `Keep-Inertial` |
| `rblock.scale.relative` | `Relative frat` |
| `rblock.scale.volume` | `Volume fvol` |
| `rblock.template` | `rblock TEmplate keyword ...` |
| `rblock.template.create` | `Create <s > keyword ...` |
| `rblock.template.create.box` | `Box fxmin fxmax <fymin fymax <fzmin fzmax >> (z-components are 3D ONLY)` |
| `rblock.template.create.circle` | `CIrcle keyword ... (2D ONLY)` |
| `rblock.template.create.circle.position` | `Position vpos` |
| `rblock.template.create.circle.radius` | `RAdius frad` |
| `rblock.template.create.circle.resolution` | `Resolution fres` |
| `rblock.template.create.cone` | `COne keyword ... (3D only)` |
| `rblock.template.create.cone.axis` | `Axis v3` |
| `rblock.template.create.cone.base` | `Base v3` |
| `rblock.template.create.cone.height` | `Height fh` |
| `rblock.template.create.cone.radius` | `RAdius fbot <ftop >` |
| `rblock.template.create.cone.resolution` | `REsolution fres` |
| `rblock.template.create.cylinder` | `CYlinder keyword ... (3D Only)` |
| `rblock.template.create.cylinder.axis` | `Axis v3` |
| `rblock.template.create.cylinder.base` | `Base v3` |
| `rblock.template.create.cylinder.height` | `Height fh` |
| `rblock.template.create.cylinder.radius` | `RAdius frad` |
| `rblock.template.create.cylinder.resolution` | `REsolution fres` |
| `rblock.template.create.density` | `Density f` |
| `rblock.template.create.facets` | `Facets v1 v2 ...` |
| `rblock.template.create.from-geometry` | `From-Geometry <set > <RANge>` |
| `rblock.template.create.group` | `Group s <Slot slot > ...` |
| `rblock.template.create.id` | `ID i` |
| `rblock.template.create.rounding` | `Rounding f <Relative>` |
| `rblock.template.create.sphere` | `Sphere keyword ... (3D ONLY)` |
| `rblock.template.create.sphere.position` | `Position vpos` |
| `rblock.template.create.sphere.radius` | `RAdius frad` |
| `rblock.template.create.sphere.resolution` | `Resolution fres` |
| `rblock.template.create.vertices` | `Vertices v1 v2 ...` |
| `rblock.template.delete` | `Delete <RANge>` |
| `rblock.thermal.attribute` | `RBlock THermal ATtribute keyword ... <range>` |
| `rblock.thermal.attribute.expansion` | `Expansion f` |
| `rblock.thermal.attribute.power-applied` | `Power-Applied f` |
| `rblock.thermal.attribute.specific-heat` | `Specific-Heat f` |
| `rblock.thermal.attribute.temperature` | `Temperature f` |
| `rblock.thermal.attribute.temperature-increment` | `Temperature-Increment f` |
| `rblock.thermal.extra` | `RBlock THermal Extra i a<range>` |
| `rblock.thermal.fix` | `RBlock THermal FIx <range>` |
| `rblock.thermal.free` | `RBlock THermal FRee <range>` |
| `rblock.thermal.group` | `RBlock THermal Group s <keyword ...> <range>` |
| `rblock.thermal.group.add` | `Add` |
| `rblock.thermal.group.remove` | `Remove` |
| `rblock.thermal.group.slot` | `Slot slot` |
| `rblock.thermal.history` | `RBlock THermal History <ID i > keyword ID i2 or v` |
| `rblock.thermal.history.power-unbalanced` | `Power-Unbalanced` |
| `rblock.thermal.history.temperature` | `Temperature` |
| `rblock.thermal.initialize` | `RBlock THermal INitialize keyword ... <range>` |
| `rblock.thermal.list` | `RBlock THermal List <keyword> <range>` |
| `rblock.thermal.list.attribute` | `Attribute <s >` |
| `rblock.thermal.list.contact` | `COntact <All>` |
| `rblock.thermal.list.extra` | `EXtra i` |
| `rblock.thermal.list.group` | `Group s` |
| `rblock.thermal.list.property` | `Property <s >` |
| `rblock.thermal.property` | `RBlock THermal Property s a<s1 a1...> <RANge>` |
| `rblock.tolerance` | `rblock TOlerance keyword ...` |
| `rblock.tolerance.constant` | `Constant fctol <RANge>` |
| `rblock.tolerance.extent` | `Extent fetol` |
| `rblock.tolerance.velocity` | `Velocity fvtol` |
| `rblock.trace` | `rblock TRace <ID id > ID id2 or v` |
| `rblock.tractions` | `RBlock TRactions keyword ... <RANge>` |
| `rblock.tractions.constant` | `Constant f1 f2 f3 f4 f5 f6 (only 3 components in 2D)` |
| `rblock.tractions.contact-active` | `Contact-Active b` |
| `rblock.tractions.direction-x` | `Direction-X v (3D ONLY)` |
| `rblock.tractions.overburden` | `Overburden f` |
| `rblock.tractions.ratio` | `Ratio f <:flt:'fy'> (3D ONLY)` |
