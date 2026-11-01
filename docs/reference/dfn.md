# DFN 命令

> 共 178 条。

| 命令 | 语法 |
|------|------|
| `fracture.aperture` | `FRACture APerture keyword <RANge>` |
| `fracture.aperture.constant` | `Constant f` |
| `fracture.aperture.dfn` | `Dfn s` |
| `fracture.aperture.fish` | `Fish s a1...an` |
| `fracture.aperture.gauss` | `Gauss fm fs` |
| `fracture.aperture.limits` | `LImits fmin fmax` |
| `fracture.aperture.log-normal` | `Log-Normal fm fs` |
| `fracture.aperture.power-law` | `Power-Law f` |
| `fracture.aperture.uniform` | `Uniform` |
| `fracture.attribute` | `FRACture ATtribute keyword <RANge>` |
| `fracture.attribute.aperture` | `APerture f` |
| `fracture.attribute.area` | `ARea f (3D only)` |
| `fracture.attribute.diameter` | `DIAmeter f (3D only)` |
| `fracture.attribute.dip` | `DIP f` |
| `fracture.attribute.dip-direction` | `Dip-Direction f (3D only)` |
| `fracture.attribute.length` | `Length f (2D only)` |
| `fracture.attribute.position` | `Position v` |
| `fracture.attribute.position-x` | `Position-X f` |
| `fracture.attribute.position-y` | `Position-Y f` |
| `fracture.attribute.position-z` | `Position-Z f (3D only)` |
| `fracture.cluster` | `FRACture CLuster keyword` |
| `fracture.cluster.group-slot` | `Group-Slot s` |
| `fracture.cluster.intersection-set` | `Intersection-Set s` |
| `fracture.combine` | `FRACture COMbine keyword <RANge>` |
| `fracture.combine.angle` | `Angle f` |
| `fracture.combine.collapse` | `Collapse` |
| `fracture.combine.distance` | `Distance f` |
| `fracture.combine.merge` | `Merge` |
| `fracture.compute` | `FRACture COMpute keyword <RANge>` |
| `fracture.compute.average-trace-length` | `Average-Trace-Length s (3D only)` |
| `fracture.compute.center-density` | `Center-Density` |
| `fracture.compute.mass-density` | `Mass-Density` |
| `fracture.compute.p10` | `P10 keyword` |
| `fracture.compute.p10.begin` | `Begin v` |
| `fracture.compute.p10.end` | `End v` |
| `fracture.compute.p10.geometry` | `GEometry s` |
| `fracture.compute.percolation` | `PErcolation` |
| `fracture.compute.trace-center-density` | `Trace-Center-Density s (3D only)` |
| `fracture.compute.trace-mass-density` | `Trace-Mass-Density s (3D only)` |
| `fracture.connectivity` | `FRACture CONnectivity keyword <RANge>` |
| `fracture.connectivity.aperture` | `Aperture` |
| `fracture.connectivity.cubic` | `Cubic` |
| `fracture.connectivity.distance` | `Distance` |
| `fracture.connectivity.extra-index` | `Extra-Index i` |
| `fracture.connectivity.intersection-set` | `Intersection-Set s` |
| `fracture.connectivity.starting-fracture` | `Starting-Fracture i` |
| `fracture.connectivity.starting-geometry` | `Starting-Geometry s` |
| `fracture.contact-model` | `FRACture Contact-Model keyword <RANgeof DFNs>` |
| `fracture.contact-model.activate` | `Activate` |
| `fracture.contact-model.deactivate` | `DEactivate` |
| `fracture.contact-model.distance` | `DIstance f` |
| `fracture.contact-model.install` | `Install` |
| `fracture.contact-model.model` | `Model s` |
| `fracture.contact-model.use-aperture` | `Use-Aperture` |
| `fracture.copy` | `FRACture COPy keyword <RANge>` |
| `fracture.copy.from-dfn` | `From-Dfn s` |
| `fracture.copy.to-dfn` | `To-Dfn s` |
| `fracture.create` | `FRACture create <keyword>` |
| `fracture.create.dfn` | `DFN s` |
| `fracture.create.dfn-dominance` | `Dfn-Dominance i` |
| `fracture.create.dip` | `DIP f` |
| `fracture.create.dip-direction` | `Dip-Direction f (3D only)` |
| `fracture.create.dominance` | `DOminance i` |
| `fracture.create.group` | `Group s <Slot slot >` |
| `fracture.create.intersection-set` | `Intersection-Set s` |
| `fracture.create.position` | `Position v` |
| `fracture.create.size` | `Size f` |
| `fracture.create.skip-errors` | `Skip-Errors` |
| `fracture.delete` | `FRACture Delete <Dfn <s > ><RANge>` |
| `fracture.dfn-extra` | `Fracture Dfn-Extra i a<RANge>` |
| `fracture.dfn-group` | `Fracture Dfn-GRoup s keyword <RANge>` |
| `fracture.dfn-group.remove` | `Remove` |
| `fracture.dfn-group.slot` | `Slot slot` |
| `fracture.export` | `FRACture EXPort keyword <RANge>` |
| `fracture.export.file` | `FILE s keyword` |
| `fracture.export.file.format` | `Format keyword` |
| `fracture.export.file.format.fishlab` | `FIshlab (3D ONLY)` |
| `fracture.export.file.format.fracman` | `FRacman (3D ONLY)` |
| `fracture.export.file.format.itasca` | `Itasca` |
| `fracture.export.intersect-with-plane` | `INtersect-With-Plane <keyword> (3D only)` |
| `fracture.export.intersect-with-plane.dip` | `Dip f` |
| `fracture.export.intersect-with-plane.dip-direction` | `Dip-Direction f` |
| `fracture.export.intersect-with-plane.origin` | `ORIGin v` |
| `fracture.export.property-file` | `Property-File s` |
| `fracture.export.template-file` | `Template-File s` |
| `fracture.extra` | `FRACture EXTra i a<RANge>` |
| `fracture.generate` | `FRACture GEnerate keyword` |
| `fracture.generate.connectivity-threshold` | `Connectivity-Threshold` |
| `fracture.generate.connectivity-threshold.box` | `Box fxl fxu fyl fyu fzl fzu (z-components are 3D only)` |
| `fracture.generate.connectivity-threshold.geometry` | `Geometry s1 <s2 >` |
| `fracture.generate.dfn` | `DFn s` |
| `fracture.generate.dfn-dominance` | `DFn-Dominance i` |
| `fracture.generate.fish-stop` | `Fish-Stop s a1...an` |
| `fracture.generate.fracture-count` | `Fracture-Count i` |
| `fracture.generate.generation-box` | `Generation-Box fxmin fxmax fymin fymax fzmin fzmax (z-components are 3D only)` |
| `fracture.generate.mass-density` | `Mass-Density f` |
| `fracture.generate.modify` | `Modify s a1...an` |
| `fracture.generate.p10` | `P10 f keyword` |
| `fracture.generate.p10.begin` | `Begin v` |
| `fracture.generate.p10.end` | `End v` |
| `fracture.generate.p10.geometry` | `Geometry s` |
| `fracture.generate.percolation` | `PErcolation fval` |
| `fracture.generate.template` | `TEmplate s` |
| `fracture.generate.tolerance-box` | `Tolerance-Box fxmin fxmax fymin fymax fzmin fzmax (z-components are 3D only)` |
| `fracture.group` | `FRACture GRoup s keyword <RANge>` |
| `fracture.group.remove` | `Remove` |
| `fracture.group.slot` | `Slot slot` |
| `fracture.import` | `FRACture IMport keyword` |
| `fracture.import.center` | `CEnter` |
| `fracture.import.clean` | `CLean` |
| `fracture.import.dfn` | `DFN s` |
| `fracture.import.dfn-dominance` | `Dfn-Dominance i` |
| `fracture.import.dominance` | `DOminance keyword` |
| `fracture.import.dominance.ordered` | `Ordered` |
| `fracture.import.dominance.random` | `Random` |
| `fracture.import.from-file` | `From-File s1 <Format keyword>` |
| `fracture.import.from-file.fishlab` | `FIshlab (3D ONLY)` |
| `fracture.import.from-file.fracman` | `FRacman (3D ONLY)` |
| `fracture.import.from-file.itasca` | `Itasca` |
| `fracture.import.from-geometry` | `From-Geometry s` |
| `fracture.import.make-disk` | `Make-Disk i (3D only)` |
| `fracture.import.make-planar` | `Make-Planar (3D only)` |
| `fracture.import.offset` | `Offset v` |
| `fracture.import.property-file` | `Property-File s` |
| `fracture.import.skip-errors` | `Skip-Errors` |
| `fracture.import.template-file` | `TEmplate-File s` |
| `fracture.import.truncate` | `Truncate` |
| `fracture.initialize` | `FRACture INItialize keyword <RANge>` |
| `fracture.intersections.automatic-update` | `FRACture INTersections Automatic-Update b` |
| `fracture.intersections.compute` | `FRACture INTersections Compute keyword <RANge>` |
| `fracture.intersections.compute.clean` | `Clean` |
| `fracture.intersections.compute.group-slot` | `GRoup-Slot s` |
| `fracture.intersections.compute.intersection-set` | `Intersection-Set s` |
| `fracture.intersections.compute.skip-errors` | `Skip-Errors (3D only)` |
| `fracture.intersections.compute.with-geometry` | `With-GEometry s <RANge>` |
| `fracture.intersections.delete` | `FRACture INTersections Delete <keyword> <RANge>` |
| `fracture.intersections.delete.intersection-set` | `Intersection-Set s` |
| `fracture.intersections.scanline` | `FRACture Intersections Scanline keyword <RANge> (3D only)` |
| `fracture.intersections.scanline.intersection-set` | `Intersection-Set s` |
| `fracture.intersections.scanline.lines` | `Lines s` |
| `fracture.intersections.scanline.surface` | `Surface s` |
| `fracture.list` | `FRACture LIst keyword <RANge>` |
| `fracture.list.attribute` | `Attribute <s >` |
| `fracture.list.extra` | `EXtra i` |
| `fracture.list.group` | `GRoup s` |
| `fracture.list.intersection` | `Intersection` |
| `fracture.list.position` | `POsition` |
| `fracture.list.property` | `PRoperty <s >` |
| `fracture.property` | `FRACture PROperty s a<s1 a1...> <RANge>` |
| `fracture.prune` | `FRACture PRUne keyword` |
| `fracture.prune.critical-number` | `Critical-Number i` |
| `fracture.prune.intersection-set` | `Intersection-Set s` |
| `fracture.set-property` | `FRACture Set-Property keyword ...` |
| `fracture.set-property.dfn` | `Dfn <Range>` |
| `fracture.set-property.fracture` | `Fracture <Range>` |
| `fracture.set-property.zone` | `Zone <Range>` |
| `fracture.template.create` | `FRACture TEmplate Create s keyword` |
| `fracture.template.create.dip-direction-limits` | `Dip-Direction-Limits fmin fmax (3D only)` |
| `fracture.template.create.dip-limits` | `Dip-Limits fmin fmax` |
| `fracture.template.create.orientation` | `Orientation s a1...an` |
| `fracture.template.create.position` | `Position s a1...an` |
| `fracture.template.create.size` | `SIze s a1...an` |
| `fracture.template.create.size-limits` | `Size-Limits fmin fmax` |
| `fracture.template.delete` | `FRACture TEmplate Delete <RANge>` |
| `fracture.template.modify-default` | `FRACture TEmplate Modify-Default keyword` |
| `fracture.template.modify-default.dip-direction-limits` | `Dip-Direction-Limits fmin fmax (3D only)` |
| `fracture.template.modify-default.dip-limits` | `Dip-Limits fmin fmax` |
| `fracture.template.modify-default.orientation` | `Orientation s a1...an` |
| `fracture.template.modify-default.position` | `Position s a1...an` |
| `fracture.template.modify-default.size` | `SIze s a1...an` |
| `fracture.template.modify-default.size-limits` | `Size-Limits fmin fmax` |
| `fracture.verify-file` | `FRACture Verify-File keyword` |
| `fracture.verify-file.file` | `FIle s` |
| `fracture.verify-file.format` | `FOrmat keyword` |
| `fracture.verify-file.format.fishlab` | `FIshlab (3D ONLY)` |
| `fracture.verify-file.format.fracman` | `FRacman` |
| `fracture.verify-file.format.itasca` | `Itasca` |
| `fracture.verify-file.property-file` | `Property-File s` |
