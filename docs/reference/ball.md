# Ball 命令

> 共 170 条。

| 命令 | 语法 |
|------|------|
| `ball.attribute` | `BAll ATtribute keyword ... <RANge>` |
| `ball.attribute.damp` | `DAmp f` |
| `ball.attribute.density` | `DEnsity f` |
| `ball.attribute.displacement` | `DIsplacement v` |
| `ball.attribute.displacement-x` | `Displacement-X f` |
| `ball.attribute.displacement-y` | `Displacement-Y f` |
| `ball.attribute.displacement-z` | `Displacement-Z f (3D ONLY)` |
| `ball.attribute.euler` | `Euler v (3D ONLY)` |
| `ball.attribute.euler-x` | `Euler-X f (3D ONLY)` |
| `ball.attribute.euler-y` | `Euler-Y f (3D ONLY)` |
| `ball.attribute.euler-z` | `Euler-Z f (3D ONLY)` |
| `ball.attribute.force-applied` | `Force-Applied v` |
| `ball.attribute.force-applied-x` | `Force-Applied-X f` |
| `ball.attribute.force-applied-y` | `Force-Applied-Y f` |
| `ball.attribute.force-applied-z` | `Force-Applied-Z f (3D ONLY)` |
| `ball.attribute.force-contact` | `Force-Contact v` |
| `ball.attribute.force-contact-x` | `Force-Contact-X f` |
| `ball.attribute.force-contact-y` | `Force-Contact-Y f` |
| `ball.attribute.force-contact-z` | `Force-Contact-Z f (3D ONLY)` |
| `ball.attribute.fragment` | `Fragment i` |
| `ball.attribute.moment-applied` | `Moment-Applied fx fy fz (y- and z- components are 3D ONLY)` |
| `ball.attribute.moment-applied-x` | `Moment-Applied-X f (3D ONLY)` |
| `ball.attribute.moment-applied-y` | `Moment-Applied-Y f (3D ONLY)` |
| `ball.attribute.moment-applied-z` | `Moment-Applied-Z f (3D ONLY)` |
| `ball.attribute.moment-contact` | `Moment-Contact fx fy fz (y- and z- components are 3D ONLY)` |
| `ball.attribute.moment-contact-x` | `Moment-Contact-X f (3D ONLY)` |
| `ball.attribute.moment-contact-y` | `Moment-Contact-Y f (3D ONLY)` |
| `ball.attribute.moment-contact-z` | `Moment-Contact-Z f (3D ONLY)` |
| `ball.attribute.position` | `Position v` |
| `ball.attribute.position-x` | `Position-X f` |
| `ball.attribute.position-y` | `Position-Y f` |
| `ball.attribute.position-z` | `Position-Z f (3D ONLY)` |
| `ball.attribute.radius` | `RAdius f` |
| `ball.attribute.rotation` | `ROtation f (2D ONLY)` |
| `ball.attribute.spin` | `Spin fx fy fz (y- and z- components are 3D ONLY)` |
| `ball.attribute.spin-x` | `Spin-X f (3D ONLY)` |
| `ball.attribute.spin-y` | `Spin-Y f (3D ONLY)` |
| `ball.attribute.spin-z` | `Spin-Z f (3D ONLY)` |
| `ball.attribute.velocity` | `Velocity v` |
| `ball.attribute.velocity-x` | `Velocity-X f` |
| `ball.attribute.velocity-y` | `Velocity-Y f` |
| `ball.attribute.velocity-z` | `Velocity-Z f (3D ONLY)` |
| `ball.create` | `BAll Create keyword ...` |
| `ball.create.group` | `Group s <Slot slot > ...` |
| `ball.create.id` | `Id i` |
| `ball.create.position` | `Position v` |
| `ball.create.position-x` | `Position-X f` |
| `ball.create.position-y` | `Position-Y f` |
| `ball.create.position-z` | `Position-Z f (3D ONLY)` |
| `ball.create.radius` | `Radius f` |
| `ball.delete` | `BAll Delete <RANge>` |
| `ball.distribute` | `BAll DIstribute keyword ... <RANge>` |
| `ball.distribute.bin` | `BIn i keyword ...` |
| `ball.distribute.bin.fish-distribution` | `Fish-Distribution s a1...an` |
| `ball.distribute.bin.gauss` | `GAuss <f >` |
| `ball.distribute.bin.group` | `GRoup s <Slot slot > ...` |
| `ball.distribute.bin.radius` | `Radius fradlow <fradhi >` |
| `ball.distribute.bin.volume-fraction` | `Volume-Fraction f` |
| `ball.distribute.box` | `BOx fxmin fxmax <fymin fymax <fzmin fzmax >> (*z*-components are 3D ONLY)` |
| `ball.distribute.number-bins` | `Number-Bins i` |
| `ball.distribute.porosity` | `Porosity f` |
| `ball.distribute.resolution` | `Resolution f` |
| `ball.export` | `BAll EXPort keyword <RANge>` |
| `ball.export.geometry` | `Geometry keyword` |
| `ball.export.geometry.positions` | `positions` |
| `ball.export.geometry.resolution` | `resolution f` |
| `ball.export.geometry.set` | `set s` |
| `ball.export.geometry.split` | `split` |
| `ball.extra` | `BAll EXTra i a<RANge>` |
| `ball.fix` | `BAll FIx keyword ... <RANge>` |
| `ball.fix.spin` | `Spin` |
| `ball.fix.spin-x` | `Spin-X (3D ONLY)` |
| `ball.fix.spin-y` | `Spin-Y (3D ONLY)` |
| `ball.fix.spin-z` | `Spin-Z (3D ONLY)` |
| `ball.fix.velocity` | `Velocity` |
| `ball.fix.velocity-x` | `Velocity-X` |
| `ball.fix.velocity-y` | `Velocity-Y` |
| `ball.fix.velocity-z` | `Velocity-Z (3D ONLY)` |
| `ball.free` | `BAll FRee keyword ... <RANge>` |
| `ball.free.spin` | `Spin` |
| `ball.free.spin-x` | `Spin-X (3D ONLY)` |
| `ball.free.spin-y` | `Spin-Y (3D ONLY)` |
| `ball.free.spin-z` | `Spin-Z (3D ONLY)` |
| `ball.free.velocity` | `Velocity` |
| `ball.free.velocity-x` | `Velocity-X` |
| `ball.free.velocity-y` | `Velocity-Y` |
| `ball.free.velocity-z` | `Velocity-Z (3D ONLY)` |
| `ball.generate` | `BAll Generate keyword ... <RANge>` |
| `ball.generate.box` | `Box fxmin fxmax <fymin fymax <fzmin fzmax >> (*z*-components are 3D ONLY)` |
| `ball.generate.cubic` | `Cubic` |
| `ball.generate.fish-distribution` | `Fish-Distribution s a1...an` |
| `ball.generate.gauss` | `GAuss <f >` |
| `ball.generate.group` | `GRoup s <Slot slot > ...` |
| `ball.generate.hexagonal` | `Hexagonal` |
| `ball.generate.id` | `Id idlow <idhi >` |
| `ball.generate.number` | `Number i` |
| `ball.generate.radius` | `Radius fradlow <fradhi >` |
| `ball.generate.tries` | `Tries i` |
| `ball.group` | `BAll Group s <keyword ...> <RANge>` |
| `ball.group.remove` | `Remove` |
| `ball.group.slot` | `Slot s` |
| `ball.history` | `BAll History <Name sid > keyword ID id or Position v` |
| `ball.history.displacement` | `Displacement` |
| `ball.history.displacement-x` | `Displacement-X` |
| `ball.history.displacement-y` | `Displacement-Y` |
| `ball.history.displacement-z` | `Displacement-Z (3D ONLY)` |
| `ball.history.euler-x` | `Euler-X (3D ONLY)` |
| `ball.history.euler-y` | `Euler-Y (3D ONLY)` |
| `ball.history.euler-z` | `Euler-Z (3D ONLY)` |
| `ball.history.force-contact` | `Force-Contact` |
| `ball.history.force-contact-x` | `Force-Contact-X` |
| `ball.history.force-contact-y` | `Force-Contact-Y` |
| `ball.history.force-contact-z` | `Force-Contact-Z (3D ONLY)` |
| `ball.history.force-unbalanced` | `Force-Unbalanced` |
| `ball.history.force-unbalanced-x` | `Force-Unbalanced-X` |
| `ball.history.force-unbalanced-y` | `Force-Unbalanced-Y` |
| `ball.history.force-unbalanced-z` | `Force-Unbalanced-Z (3D ONLY)` |
| `ball.history.moment-contact` | `Moment-Contact` |
| `ball.history.moment-contact-x` | `Moment-Contact-X (3D ONLY)` |
| `ball.history.moment-contact-y` | `Moment-Contact-Y (3D ONLY)` |
| `ball.history.moment-contact-z` | `Moment-Contact-Z (3D ONLY)` |
| `ball.history.moment-unbalanced` | `Moment-Unbalanced` |
| `ball.history.moment-unbalanced-x` | `Moment-Unbalanced-X (3D ONLY)` |
| `ball.history.moment-unbalanced-y` | `Moment-Unbalanced-Y (3D ONLY)` |
| `ball.history.moment-unbalanced-z` | `Moment-Unbalanced-Z (3D ONLY)` |
| `ball.history.position-x` | `Position-X` |
| `ball.history.position-y` | `Position-Y` |
| `ball.history.position-z` | `Position-Z (3D ONLY)` |
| `ball.history.rotation` | `ROtation (2D ONLY)` |
| `ball.history.spin` | `Spin` |
| `ball.history.spin-x` | `Spin-X (3D ONLY)` |
| `ball.history.spin-y` | `Spin-Y (3D ONLY)` |
| `ball.history.spin-z` | `Spin-Z (3D ONLY)` |
| `ball.history.velocity` | `Velocity` |
| `ball.history.velocity-x` | `Velocity-X` |
| `ball.history.velocity-y` | `Velocity-Y` |
| `ball.history.velocity-z` | `Velocity-Z` |
| `ball.initialize` | `BAll INitialize keyword ... <RANge>` |
| `ball.list` | `BAll LIst <keyword> <RANge>` |
| `ball.list.attribute` | `Attribute <keyword>` |
| `ball.list.contact` | `COntact <All>` |
| `ball.list.extra` | `EXtra i` |
| `ball.list.group` | `Group s` |
| `ball.list.property` | `Property <s >` |
| `ball.list.result` | `Result` |
| `ball.property` | `BAll Property s a<s1 a21...> <RANge>` |
| `ball.results` | `BAll Results keyword ...` |
| `ball.results.active` | `ACtive b` |
| `ball.results.add-attribute` | `ADd-Attribute s` |
| `ball.results.remove-attribute` | `Remove-Attribute s` |
| `ball.tolerance` | `BAll TOlerance keyword ...` |
| `ball.tolerance.constant` | `Constant f <RANge>` |
| `ball.tolerance.extent` | `Extent f` |
| `ball.tolerance.velocity` | `Velocity f` |
| `ball.trace` | `BAll TRace <ID id > ID id2 or v` |
| `ball.tractions` | `BAll TRactions keyword ... <RANge>` |
| `ball.tractions.angular-tolerance` | `Angular-tolerance f` |
| `ball.tractions.boundary-group` | `Boundary-Group s <Slot slot > ...` |
| `ball.tractions.constant` | `Constant f1 f2 f3 f4 f5 f6 (only 3 components in 2D)` |
| `ball.tractions.contact-active` | `Contact-Active b` |
| `ball.tractions.contact-create` | `Contact-Create b` |
| `ball.tractions.direction-x` | `Direction-X v (3D ONLY)` |
| `ball.tractions.layered` | `Layered b` |
| `ball.tractions.overburden` | `Overburden f` |
| `ball.tractions.periodicity` | `PEriodicity bx by bz (z-component is 3D ONLY)` |
| `ball.tractions.polydisperse` | `Polydisperse b` |
| `ball.tractions.ratio` | `Ratio f <:flt:'fy'> (3D ONLY)` |
| `ball.tractions.update-area` | `Update-Area b` |
| `ball.tractions.update-position` | `Update-Position b` |
| `ball.tractions.update-volume` | `Update-Volume b` |
