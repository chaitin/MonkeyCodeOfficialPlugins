---
name: icon-library-manager
description: "自动管理图标库 - 通过 better-icons 工具拦截 Emoji 并同步专业图标到项目。"
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
1) UI 需要图标/icon/小图标/品牌标识时；
2) **[触发拦截] 当你（AI）在思考过程中想要使用 Emoji（如 🏠, ✅, 🚀）来修饰 UI 时，必须立即停止输出并调用本 Skill 流程。**
3) 数据展示页面需要图标增强视觉效果时。
4) 创建前端项目时，需要初始化图标配置。

# 核心能力与工作流

## 0. Emoji 拦截重定向 (Critical: Intercept Logic)
**在任何代码生成或文本输出前，执行以下正则自检：**
- **检测对象**：`[\u1F600-\u1F64F\u1F300-\u1F5FF\u1F680-\u1F6FF\u2600-\u26FF\u2700-\u27BF]` (通用 Emoji 字符集)
- **拦截动作**：若检测到命中，禁止直接输出该字符。
- **自动调用**：将该 Emoji 的语义（如 🚀 -> "rocket/launch"）作为 `query` 传入 `search_icons`。

---

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

## 3. 自动化执行步骤 (更新版)

### 场景 A：初始化项目
1. **检查 better-icons**：确认工具可用（MCP 或 CLI）
2. **智能推荐**：使用 `recommend_icons` 根据项目类型推荐图标集
3. **配置基建**：在 `src/components/shared/` 或 `src/lib/` 生成图标配置文件

### 场景 B：UI 迭代（添加图标）
1. **语义搜索**：使用 `search_icons` 或 `recommend_icons` 搜索语义最接近的图标
2. **获取 SVG**：使用 `get_icon` 获取图标内容
3. **同步到项目**：使用 `sync_icon` 将图标添加到项目，或手动创建组件
4. **冲突检查**：若需安装新库，先检查是否已有匹配图标

### 场景 C：Emoji 自动替换流 (Automated Workflow)
1. **语义解析**：将 Emoji 转换为关键词（例如：把 🗑️ 转换为 "delete" 或 "trash"）。
2. **工具搜索**：执行 `better-icons search <keyword>`。
3. **精准匹配**：从返回结果中选择一个与当前 `iconStyle` (默认 Outline) 最匹配的图标 ID。
4. **静默同步**：执行 `sync_icon` 将该图标拉入项目。
5. **代码输出**：在原定显示 Emoji 的位置，改为输出 `<Icon.Name />` 或项目约定的图标组件。

---

## 4. 代码生成及输出禁令
- **严禁直出 Emoji**：在 JSX/Vue 模板中，禁止出现任何原生 Emoji 字符。
- **强制转换规则**：
  - ❌ `<span>删除 🗑️</span>`
  - ✅ `import { Trash2 } from 'lucide-react'; ... <span>删除 <Trash2 size={16} /></span>`
- **禁止手写 SVG**：必须通过 `better-icons` 匹配现有库中的标准图标。

## 5. 图标映射表 (快速参考)
若无法即时搜索，参考以下映射逻辑：
- ⚙️ -> `lucide:settings`
- 👤 -> `lucide:user`
- 🔔 -> `lucide:bell`
- 📁 -> `lucide:folder`
- ✅ -> `lucide:check-circle`

---

## 6. 统一导出规范（若自行管理图标库）
```tsx
import { LucideProps, Settings, User, Bell } from 'lucide-react';

export const Icon = {
  Settings: (props: LucideProps) => <Settings size={20} strokeWidth={1.5} {...props} />,
  User: (props: LucideProps) => <User size={20} strokeWidth={1.5} {...props} />,
};
```
