# 单轴压缩

单轴压缩试验（Uniaxial Compression Test，UCS）是 PFC 中最经典、也最常作为**参数标定基准**的算例：建立一颗颗黏结的颗粒试样，施加轴向压缩，观察应力-应变曲线、峰值强度与裂纹演化，并与室内试验或目标力学参数对比。

> 命令以 PFC 6.0/7.0 为准，`;` 为注释。建模基础见「[基本建模流程](../guide/basic-workflow)」，接触模型原理见「[接触模型](../theory/contact-models)」。

## 一、试样与材料

- 试样尺寸：宽 50 mm × 高 100 mm（标准岩心比例 1:2）。
- 颗粒：用**线性平行键模型**（`linearpbond`）黏结，模拟岩石。
- 单位：本例采用 SI（m、kg、Pa）。

| 参数 | 值（示例） | 说明 |
|------|-----------|------|
| 颗粒半径 | 1.5–2.5 mm | 兼顾分辨率与计算量 |
| 密度 `density` | 2650 kg/m³ | 岩石密度 |
| 有效模量 `emod` | 1e9 Pa | 需按目标弹性模量标定 |
| 刚度比 `kratio` | 1.5 | 法切刚度比 |
| 抗拉强度 `pb_ten` | 5e6 Pa | 平行键抗拉强度 |
| 内聚力 `pb_coh` | 1e7 Pa | 平行键内聚力 |

## 二、建模步骤

### 1. 生成试样并分组

```text
model new
model domain extent -0.05 0.05 -0.05 0.05

ball distribute porosity 0.15 radius 0.0015 0.0025 box -0.025 0.025 -0.05 0.05
ball group 'specimen' range box -0.025 0.025 -0.05 0.05
ball attribute density 2650 damp 0.7
```

### 2. 创建边界墙

上下两块**压板**（加载用）+ 左右**侧墙**（生成/平衡阶段约束，加载前删除）：

```text
wall create vertices (-0.03,-0.05) (0.03,-0.05) name 'bottom'
wall create vertices (-0.03, 0.05) (0.03, 0.05) name 'top'
wall create vertices (-0.03,-0.05) (-0.03, 0.05) name 'left'
wall create vertices ( 0.03,-0.05) ( 0.03, 0.05) name 'right'
```

### 3. 赋接触模型（线性平行键）

```text
contact cmat default type ball-ball model linearpbond property emod 1e9 kratio 1.5 fric 0.5 pb_emod 1e9 pb_kratio 1.5 pb_ten 5e6 pb_coh 1e7
```

### 4. 初始平衡

```text
model solve
model save 'ucs_bonded'
```

> 若初始重叠较大，可先 `ball attribute radius multiply 0.8` 缩小颗粒，再分阶段放大并反复 `model solve`，最后再赋黏结。

## 三、施加单轴压缩

删除侧墙以允许横向变形，然后让上下压板相向运动：

```text
wall delete range group 'left'
wall delete range group 'right'

wall attribute velocity-y -0.001 range group 'top'     ; 向下
wall attribute velocity-y  0.001 range group 'bottom'  ; 向上
```

**两种加载控制方式**：

- **位移控制**（上面这种）：固定压板速度，简单稳定，UCS 常用。
- **伺服控制**（恒定应力速率）：用 `wall servo` 自动调整压板速度：

```text
wall servo activate range group 'top'
wall servo force -1e5 range group 'top'      ; 目标力 = 目标应力 × 试样宽度
wall servo velocity-max 0.001 range group 'top'
```

## 四、监测与结果

**轴向应力** = 压板反力 / 试样宽度（2D 单位厚度）；**轴向应变** = 压板位移 / 试样原高。

用 FISH 记录应力-应变与裂纹数，导出到文件绘制曲线：

```text
[global wp_top = wall.find(1)]
history interval 100
[history = -wall.force.contact.y(wp_top) / 0.05]   ; 轴向应力（压为正）
```

典型结果：

- **应力-应变曲线**：先近似线弹性上升 → 达峰值强度 → 峰后软化。
- **峰值强度**：对应单轴抗压强度 $\sigma_c$。
- **破坏形态**：试样中部出现宏观剪切带或劈裂裂纹（用 `ball fragment` 或裂纹几何统计）。

## 五、完整示例脚本

```text
model new
model domain extent -0.05 0.05 -0.05 0.05

; 生成试样
ball distribute porosity 0.15 radius 0.0015 0.0025 box -0.025 0.025 -0.05 0.05
ball group 'specimen' range box -0.025 0.025 -0.05 0.05
ball attribute density 2650 damp 0.7

; 边界墙
wall create vertices (-0.03,-0.05) (0.03,-0.05) name 'bottom'
wall create vertices (-0.03, 0.05) (0.03, 0.05) name 'top'
wall create vertices (-0.03,-0.05) (-0.03, 0.05) name 'left'
wall create vertices ( 0.03,-0.05) ( 0.03, 0.05) name 'right'

; 线性平行键
contact cmat default type ball-ball model linearpbond property emod 1e9 kratio 1.5 fric 0.5 pb_emod 1e9 pb_kratio 1.5 pb_ten 5e6 pb_coh 1e7

; 初始平衡
model solve
model save 'ucs_bonded'

; 施加单轴压缩
wall delete range group 'left'
wall delete range group 'right'
wall attribute velocity-y -0.001 range group 'top'
wall attribute velocity-y  0.001 range group 'bottom'
model cycle 50000

model save 'ucs_failed'
```

## 六、参数标定提示

- 宏观**弹性模量**主要由 `emod`（及 `pb_emod`）控制，**峰值强度**主要由 `pb_ten`、`pb_coh` 控制，**摩擦角**由 `fric` 控制。
- 平行键模型的一个已知问题是**压拉强度比偏低**（模拟值 $\sigma_c/\sigma_t$ 往往小于真实岩石）。若需更真实，可改用**平直节理模型**（`flatjoint`），它能抵抗颗粒转动、给出更合理的压拉比（见 Itasca rocktest 示例的对比）。

## 相关

- [基本建模流程](../guide/basic-workflow)
- [接触模型](../theory/contact-models) / [参数标定](../theory/material-calibration)
- [Wall 命令](/reference/wall) / [接触模型命令](/reference/contact-models) / [Ball FISH 函数](/reference/fish-ball)
