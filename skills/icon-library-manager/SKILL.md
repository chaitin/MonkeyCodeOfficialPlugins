---
name: icon-library-manager
description: "自动管理图标库 - 通过 better-icons 工具搜索、获取并同步图标到项目。"
arguments:
  - name: projectPath
    description: 前端项目根目录的绝对路径
    required: true
  - name: framework
    description: 识别项目框架 (React/Vue/Next.js/Vite)
    required: false
  - name: iconStyle
    description: 偏好的风格 (Outline/Filled/Thin/Sharp)
    default: "Outline"
---

# 什么时候用
1) UI 需要图标/icon/小图标/品牌标识/按钮前加图标/列表项带图标时；2) AI 想用或输出 emoji 时（必须提醒并用图标替代）；3) 数据展示页面（表格、统计视图、Dashboard）需要通过图标提升视觉效果时。

# 核心能力与工作流

## 1. 优先使用 better-icons 工具
优先调用 better-icons 的 MCP 工具来搜索和获取图标，而非直接安装整个图标库。

### MCP 工具使用顺序
1. **搜索图标** (`search_icons` / `recommend_icons`)：根据语义描述搜索合适图标
2. **获取图标** (`get_icon`)：获取具体图标的 SVG 或组件
3. **同步到项目** (`sync_icon`)：直接将图标同步到项目文件中

### CLI 备选方案
若 MCP 不可用，可使用 CLI：
```bash
better-icons search <query> [--prefix <prefix>] [--limit <n>]
better-icons get <icon-id> [--color <color>] [--size <px>]
```

### 图标 ID 格式
`prefix:name` - 例如 `lucide:home`, `mdi:arrow-right`, `heroicons:check`

### 推荐图标集
`lucide`, `mdi`, `heroicons`, `tabler`, `ph`, `ri`, `solar`, `iconamoon`

---

## 2. 智能选型策略 (Selection Logic)
当接收到 `productDescription` 或无法通过 better-icons 找到合适图标时，按以下优先级选择：
- **企业级/B端/通用**: Lucide (首选，属性最全，支持 Tree-shaking)。
- **精细/多风格 (Thin/Bold)**: Phosphor Icons。
- **极简/高质感**: Heroicons (配合 Tailwind CSS)。
- **高密度/工具类**: Tabler Icons。
- **国内/特定业务**: Remix Icon。

---

## 3. 自动化执行步骤

### 场景 A：初始化项目
1. **检查 better-icons**：确认工具可用（MCP 或 CLI）
2. **智能推荐**：使用 `recommend_icons` 根据项目类型推荐图标集
3. **配置基建**：在 `src/components/shared/` 或 `src/lib/` 生成图标配置文件

### 场景 B：UI 迭代（添加图标）
1. **语义搜索**：使用 `search_icons` 或 `recommend_icons` 搜索语义最接近的图标
2. **获取 SVG**：使用 `get_icon` 获取图标内容
3. **同步到项目**：使用 `sync_icon` 将图标添加到项目，或手动创建组件
4. **冲突检查**：若需安装新库，先检查是否已有匹配图标

### 场景 C：Emoji 拦截
- 若需求/示例中出现 emoji，先提示"请改用图标库"
- 使用 `find_similar_icons` 找同风格替代，必要时用 icon+文本

---

## 4. 代码生成标准
- **禁用 Emoji**：严禁在 UI 渲染逻辑中硬编码 Emoji。
- **优先工具获取**：优先使用 better-icons 工具获取图标，而非安装整个图标库。
- **禁止手写 SVG**：严禁自己编写 SVG 代码代替图标库图标。必须先通过 better-icons 搜索匹配图标。
- **统一导出规范**（若自行管理图标库）：
  ```tsx
  import { LucideProps, Settings, User, Bell } from 'lucide-react';

  export const Icon = {
    Settings: (props: LucideProps) => <Settings size={20} strokeWidth={1.5} {...props} />,
    User: (props: LucideProps) => <User size={20} strokeWidth={1.5} {...props} />,
  };
  ```
