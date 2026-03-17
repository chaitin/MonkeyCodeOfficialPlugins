---
name: icon-library-manager
description: "自动管理图标库 - 创建项目时安装图标库，编辑时添加缺失图标。触发时机：1) UI 需要图标时；2) AI 想用或输出 emoji 时（必须提醒并用图标替代）。"
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

# 核心能力与工作流

## 1. 智能选型策略 (Selection Logic)
当接收到 `productDescription` 时，按以下优先级选择：
- **企业级/B端/通用**: Lucide (首选，属性最全，支持 Tree-shaking)。
- **精细/多风格 (Thin/Bold)**: Phosphor Icons。
- **极简/高质感**: Heroicons (配合 Tailwind CSS)。
- **高密度/工具类**: Tabler Icons。
- **国内/特定业务**: Remix Icon。

## 2. 自动化执行步骤
### 场景 A：初始化项目
1. **环境侦测**：检查 `package.json` 确定包管理器 (pnpm > yarn > npm) 和框架。
2. **静默安装**：执行安装命令 (例如 `pnpm add lucide-react`)。
3. **配置基建**：在 `src/components/shared/` 或 `src/lib/` 自动生成 `icon-registry.tsx`。

### 场景 B：UI 迭代（添加缺失图标）
1. **语义对齐**：当 AI 意图使用 Emoji（如 ⚙️）或 描述（如 "设置"）时，搜索已安装库中语义最接近的图标（如 `Settings`）。
2. **冲突检查**：优先使用现有库。若风格差异过大，才考虑引入第二个库。
3. **按需导出**：将新图标追加到全局图标组件库中。
4. **添加到 Icons 组件**：确保新图标已注册到 Icons 集中，避免使用 emoji 作为备选。
5. **Emoji 拦截**：如果需求/示例中出现 emoji，先提示"请改用图标库"，提供同风格图标替代，必要时用 icon+文本而非 emoji。

## 3. 代码生成标准
- **禁用 Emoji**：严禁在 UI 渲染逻辑中硬编码 Emoji。
- **统一导出规范**：
  ```tsx
  // 推荐：集中管理，方便全局替换尺寸和线宽
  import { LucideProps, Settings, User, Bell } from 'lucide-react';

  export const Icon = {
    Settings: (props: LucideProps) => <Settings size={20} strokeWidth={1.5} {...props} />,
    User: (props: LucideProps) => <User size={20} strokeWidth={1.5} {...props} />,
  };
  ```
