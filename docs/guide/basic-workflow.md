# 基本建模流程

PFC2D 的建模遵循一个标准流程。理解这条主线，就能举一反三地搭建各种模型。下面以「在方盒中生成颗粒并压实到平衡」为例，走完一个最小但完整的流程。

> 命令语法以 PFC 6.0/7.0 为准，`;` 开头为注释。完整命令见「[官方文档速查](/reference/)」。

## 流程总览

1. 新建模型、设置**模型域**
2. 生成**颗粒**
3. 创建**墙体**（边界）
4. 赋**接触模型**与**材料属性**
5. **初始平衡**
6. 施加荷载、运行**模拟**
7. **输出**与后处理

## 第 1 步：新建模型与设置模型域

```text
model new                                  ; 清空当前模型
model domain extent -10 10 -10 10          ; 设置计算域（xmin xmax ymin ymax）
```

- 模型域（domain）是所有颗粒必须位于其内的矩形区域。颗粒越界会被销毁。
- 域要留出足够的空间，避免颗粒在压缩过程中跑出边界。

## 第 2 步：生成颗粒

**创建单个颗粒**（指定半径与位置）：

```text
ball create radius 0.5 position 0 0         ; 在 (0,0) 生成半径 0.5 的球
```

**批量生成**（按目标孔隙率填充一个盒子）：

```text
ball distribute porosity 0.15 radius 0.3 0.5 box -8 8 -8 8
```

- `porosity` 为目标孔隙率；`radius` 给出半径区间；`box` 指定填充范围。
- 生成时若颗粒重叠，可先用较小的半径生成，再逐步放大压实（见第 5 步）。

**分组**（便于后续对不同区域赋属性）：

```text
ball group 'sample' range box -8 8 -8 8
```

## 第 3 步：创建墙体（边界）

用墙体围成加载边界或试样边界：

```text
wall create vertices (-8,-8) (8,-8) (8,8) (-8,8) name 'box'
```

- `vertices` 依次给出多边形顶点（首尾自动闭合）。
- 墙体可设置速度、伺服控制，用于施加边界位移或围压。

## 第 4 步：赋接触模型与材料属性

**接触模型**：指定球-球接触使用哪种模型及参数。例如线性模型：

```text
contact cmat default type ball-ball model linear property emod 1e9 kratio 1.5 fric 0.5
```

- `emod` 为有效模量，`kratio` 为法切刚度比，`fric` 为摩擦系数。
- 接触模型的种类与选择见「[接触模型](../theory/contact-models)」。

**颗粒属性**：

```text
ball attribute density 2650 damp 0.7          ; 密度与局部阻尼
```

## 第 5 步：初始平衡

在施加载荷前，先让颗粒在重力（如有）或重叠作用下达到初始平衡状态：

```text
model gravity 0 -9.81                          ; 如需重力
model solve                                    ; 求解到平衡
```

或按指定步数循环：

```text
model cycle 10000
```

- `model solve` 会自动判断收敛（默认按平均力比）；`model cycle` 是固定步数。
- 若颗粒重叠严重，可先 `ball attribute radius multiply 1.6` 缩小颗粒，再分阶段放大、反复求解。

## 第 6 步：施加荷载与模拟

常见加载方式：

- **速度边界**：给墙或颗粒设速度。
- **伺服控制**：让墙自动调整速度以维持目标应力（用于施加围压）。
- **位移控制**：固定速度匀速压缩，直到达到目标位移。

示例（给顶部墙一个向下的速度）：

```text
wall attribute velocity-y -0.1 range group 'top'
model cycle 20000
```

## 第 7 步：结果输出与后处理

**保存模型**（二进制，可随时 `model restore` 恢复）：

```text
model save 'sample_after_settle'
```

**记录历史变量**（应力、应变等），配合 FISH 测量函数输出：

```text
history interval 100
ball history stress-xx id 1
```

**导出数据**：用 FISH 遍历颗粒，把位置、速度、接触力等写入文本文件，再用外部工具绘图。

## 完整最小示例

```text
model new
model domain extent -10 10 -10 10

; 生成颗粒
ball distribute porosity 0.15 radius 0.3 0.5 box -8 8 -8 8
ball group 'sample' range box -8 8 -8 8
ball attribute density 2650 damp 0.7

; 边界墙
wall create vertices (-8,-8) (8,-8) (8,8) (-8,8) name 'box'

; 接触模型与属性
contact cmat default type ball-ball model linear property emod 1e9 kratio 1.5 fric 0.5

; 初始平衡
model solve
model save 'sample_settled'
```

## 相关

- [接触模型](../theory/contact-models) — 接触模型的原理与选型
- [Ball 命令](/reference/ball) / [Wall 命令](/reference/wall) / [Model / Program 命令](/reference/kernel)
- [单轴压缩](../examples/uniaxial-compression) — 一个完整工程案例
