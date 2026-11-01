# Wall 命令

> 共 179 条。

| 命令 | 语法 |
|------|------|
| `wall.active-sides` | `Wall ACtive-Sides keyword <RANge>` |
| `wall.active-sides.both` | `BOTH` |
| `wall.active-sides.bottom` | `BOTTom` |
| `wall.active-sides.neither` | `Neither` |
| `wall.active-sides.top` | `Top` |
| `wall.addfacet` | `Wall ADdfacet keyword ...` |
| `wall.addfacet.facetid` | `Facetid ifacet` |
| `wall.addfacet.group` | `GRoup keyword ...` |
| `wall.addfacet.group.name` | `Name s` |
| `wall.addfacet.group.slot` | `Slot slot` |
| `wall.addfacet.id` | `Id id` |
| `wall.addfacet.name` | `Name s` |
| `wall.addfacet.vertex` | `Vertex ivert or vpos` |
| `wall.attribute` | `Wall ATtribute <Facet> <Vertex> keyword ... <RANge>` |
| `wall.attribute.cutoff-angle` | `Cutoff-angle f` |
| `wall.attribute.displacement` | `DIsplacement v` |
| `wall.attribute.displacement-x` | `Displacement-X f` |
| `wall.attribute.displacement-y` | `Displacement-Y f` |
| `wall.attribute.displacement-z` | `Displacement-Z f (3D ONLY)` |
| `wall.attribute.euler` | `Euler v (3D ONLY)` |
| `wall.attribute.euler-x` | `Euler-X f (3D ONLY)` |
| `wall.attribute.euler-y` | `Euler-Y f (3D ONLY)` |
| `wall.attribute.euler-z` | `Euler-Z f (3D ONLY)` |
| `wall.attribute.fragment` | `Fragment i` |
| `wall.attribute.position` | `Position v` |
| `wall.attribute.position-x` | `Position-X f` |
| `wall.attribute.position-y` | `Position-Y f` |
| `wall.attribute.position-z` | `Position-Z f` |
| `wall.attribute.rotation-center` | `Rotation-Center v` |
| `wall.attribute.rotation-center-x` | `Rotation-Center-X f` |
| `wall.attribute.rotation-center-y` | `Rotation-Center-Y f` |
| `wall.attribute.rotation-center-z` | `Rotation-Center-Z f (3D ONLY)` |
| `wall.attribute.spin` | `Spin fx fy fz (y- and z- components are 3D ONLY)` |
| `wall.attribute.spin-x` | `Spin-X f (3D ONLY)` |
| `wall.attribute.spin-y` | `Spin-Y f (3D ONLY)` |
| `wall.attribute.spin-z` | `Spin-Z f (3D ONLY)` |
| `wall.attribute.velocity` | `VElocity v` |
| `wall.attribute.velocity-conveyor` | `Velocity-Conveyor v` |
| `wall.attribute.velocity-conveyor-x` | `Velocity-Conveyor-X f` |
| `wall.attribute.velocity-conveyor-y` | `Velocity-Conveyor-Y f` |
| `wall.attribute.velocity-conveyor-z` | `Velocity-Conveyor-Z f (3D ONLY)` |
| `wall.attribute.velocity-x` | `Velocity-X f` |
| `wall.attribute.velocity-y` | `Velocity-Y f` |
| `wall.attribute.velocity-z` | `Velocity-Z f (3D ONLY)` |
| `wall.create` | `Wall CReate keyword ...` |
| `wall.create.group` | `GRoup` |
| `wall.create.id` | `Id id` |
| `wall.create.name` | `Name s` |
| `wall.create.vertices` | `Vertices vert1` |
| `wall.delete` | `Wall Delete <keyword> <RANge>` |
| `wall.delete.facets` | `Facets` |
| `wall.delete.walls` | `Walls` |
| `wall.export` | `Wall EXPort keyword <RANge>` |
| `wall.export.geometry` | `Geometry keyword` |
| `wall.export.geometry.set` | `set s` |
| `wall.export.geometry.split` | `split` |
| `wall.extra` | `Wall Extra i a<Facet> <RANge>` |
| `wall.generate` | `Wall Generate keyword ...` |
| `wall.generate.box` | `Box fxmin fxmax fymin fymax fzmin fzmax <One-wall> (*z*-components are 3D ONLY)` |
| `wall.generate.circle` | `CIrcle keyword ... (2D ONLY)` |
| `wall.generate.circle.position` | `Position vpos` |
| `wall.generate.circle.radius` | `RAdius frad` |
| `wall.generate.circle.resolution` | `Resolution fres` |
| `wall.generate.cone` | `COne keyword ... (3D ONLY)` |
| `wall.generate.cone.axis` | `Axis faxisx faxisy faxisz` |
| `wall.generate.cone.base` | `Base v` |
| `wall.generate.cone.cap` | `Cap bbottom <btop >` |
| `wall.generate.cone.height` | `Height fheight` |
| `wall.generate.cone.one-wall` | `One-wall` |
| `wall.generate.cone.radius` | `RAdius fradbot <fradtop >` |
| `wall.generate.cone.resolution` | `REsolution fres` |
| `wall.generate.cylinder` | `CYlinder keyword ... (3D ONLY)` |
| `wall.generate.cylinder.axis` | `Axis v` |
| `wall.generate.cylinder.base` | `Base v` |
| `wall.generate.cylinder.cap` | `Cap bbottom <btop >` |
| `wall.generate.cylinder.height` | `Height fheight` |
| `wall.generate.cylinder.one-wall` | `One-wall` |
| `wall.generate.cylinder.radius` | `RAdius frad` |
| `wall.generate.cylinder.resolution` | `REsolution fres` |
| `wall.generate.disk` | `Disk keyword ... (3D ONLY)` |
| `wall.generate.disk.dip` | `DIP fdip` |
| `wall.generate.disk.dip-direction` | `DIP-Direction fddir` |
| `wall.generate.disk.position` | `Position v` |
| `wall.generate.disk.radius` | `RAdius frad` |
| `wall.generate.disk.resolution` | `Resolution fres` |
| `wall.generate.group` | `GRoup s <Slot slot > <Facet> ...` |
| `wall.generate.id` | `Id id` |
| `wall.generate.name` | `Name s` |
| `wall.generate.plane` | `PLAne keyword ...` |
| `wall.generate.plane.dip` | `DIP fdip` |
| `wall.generate.plane.dip-direction` | `DIP-Direction fddir (3D ONLY)` |
| `wall.generate.plane.position` | `Position v` |
| `wall.generate.point` | `POInt keyword ...` |
| `wall.generate.point.position` | `Position vpos` |
| `wall.generate.point.resolution` | `Resolution fres` |
| `wall.generate.polygon` | `POLygon vpos ... <make-planar> <triangulate> (3D ONLY)` |
| `wall.generate.sphere` | `Sphere keyword ... (3D ONLY)` |
| `wall.generate.sphere.position` | `Position vpos` |
| `wall.generate.sphere.radius` | `RAdius frad` |
| `wall.generate.sphere.resolution` | `Resolution fres` |
| `wall.group` | `Wall Group s keyword ... <Facet> <RANge>` |
| `wall.group.remove` | `Remove` |
| `wall.group.slot` | `Slot s` |
| `wall.history` | `Wall History <Name sid > keyword ID id or Name s or Position v` |
| `wall.history.displacement` | `Displacement` |
| `wall.history.displacement-x` | `Displacement-X` |
| `wall.history.displacement-y` | `Displacement-Y` |
| `wall.history.displacement-z` | `Displacement-Z (3D ONLY)` |
| `wall.history.euler-x` | `Euler-X (3D ONLY)` |
| `wall.history.euler-y` | `Euler-Y (3D ONLY)` |
| `wall.history.euler-z` | `Euler-Z (3D ONLY)` |
| `wall.history.force-contact` | `Force-Contact` |
| `wall.history.force-contact-x` | `Force-Contact-X` |
| `wall.history.force-contact-y` | `Force-Contact-Y` |
| `wall.history.force-contact-z` | `Force-Contact-Z (3D ONLY)` |
| `wall.history.moment-contact` | `Moment-Contact` |
| `wall.history.moment-contact-x` | `Moment-Contact-X (3D ONLY)` |
| `wall.history.moment-contact-y` | `Moment-Contact-Y (3D ONLY)` |
| `wall.history.moment-contact-z` | `Moment-Contact-Z (3D ONLY)` |
| `wall.history.position-x` | `Position-X` |
| `wall.history.position-y` | `Position-Y` |
| `wall.history.position-z` | `Position-Z (3D ONLY)` |
| `wall.history.rotation` | `ROtation (2D ONLY)` |
| `wall.history.spin` | `Spin` |
| `wall.history.spin-x` | `Spin-X (3D ONLY)` |
| `wall.history.spin-y` | `Spin-Y (3D ONLY)` |
| `wall.history.spin-z` | `Spin-Z (3D ONLY)` |
| `wall.history.velocity` | `Velocity` |
| `wall.history.velocity-x` | `Velocity-X` |
| `wall.history.velocity-y` | `Velocity-Y` |
| `wall.history.velocity-z` | `Velocity-Z` |
| `wall.import` | `Wall IMport keyword ... <RANge>` |
| `wall.import.filename` | `FIlename s` |
| `wall.import.from-geometry` | `FRom-Geometry s` |
| `wall.import.from-geometry.clean` | `Clean` |
| `wall.import.from-geometry.keepid` | `Keepid` |
| `wall.import.from-geometry.seed` | `Seed i` |
| `wall.import.group` | `GRoup s <Slot slot > <Facet> ...` |
| `wall.import.id` | `Id id` |
| `wall.import.name` | `NAme s` |
| `wall.import.skip-errors` | `Skip-Errors` |
| `wall.initialize` | `Wall INitialize keyword ... <RANge>` |
| `wall.list` | `Wall List <keyword> <RANge>` |
| `wall.list.attribute` | `Attribute <keyword>` |
| `wall.list.contact` | `COntact <All>` |
| `wall.list.extra` | `EXtra i <Facet>` |
| `wall.list.group` | `Group s <Facet>` |
| `wall.list.property` | `Property <s >` |
| `wall.list.result` | `Result` |
| `wall.property` | `Wall Property s a<s1 a1...> <RANge>` |
| `wall.resolution` | `Wall RESOlution keyword` |
| `wall.resolution.full` | `Full` |
| `wall.resolution.none` | `None` |
| `wall.resolution.reduced` | `Reduced` |
| `wall.results` | `Wall RESults keyword ...` |
| `wall.results.active` | `ACtive b` |
| `wall.results.add-attribute` | `ADd-Attribute s` |
| `wall.results.remove-attribute` | `Remove-Attribute s` |
| `wall.rotate` | `Wall ROtate keyword ... <RANge>` |
| `wall.rotate.angle` | `ANgle fang` |
| `wall.rotate.axis` | `AXis vaxis` |
| `wall.rotate.point` | `Point vrot` |
| `wall.rotate.update-orientation` | `Update-Orientation b` |
| `wall.servo` | `Wall Servo keyword ... <RANge>` |
| `wall.servo.activate` | `Activate b` |
| `wall.servo.force` | `Force v` |
| `wall.servo.force-x` | `Force-X f` |
| `wall.servo.force-y` | `Force-Y f` |
| `wall.servo.force-z` | `Force-Z f (3D ONLY)` |
| `wall.servo.gain-factor` | `GAIN-Factor f` |
| `wall.servo.gain-update` | `GAIN-Update i` |
| `wall.servo.velocity-max` | `Velocity-Max f` |
| `wall.tolerance` | `Wall TOlerance keyword ...` |
| `wall.tolerance.constant` | `Constant f <RANge>` |
| `wall.tolerance.extent` | `Extent f` |
| `wall.tolerance.velocity` | `Velocity f` |
| `wall.velocity-conveyor` | `Wall Velocity-COnveyor keyword ... <RANGe...>` |
| `wall.velocity-conveyor.point` | `Point vpos` |
| `wall.velocity-conveyor.spin` | `Spin fspinx fspiny fspinz (y- and z- components are 3D ONLY)` |
