---
name: mui-helper
description: MUI (Material-UI) 组件库使用指南和参考文档。在需要使用 MUI 组件开发 UI 时自动触发：(1) 创建或修改使用 Material-UI 的 UI 组件，(2) 解决 MUI 组件实现问题，(3) 查询 MUI 组件属性和 API，(4) 实现 MUI 布局和主题定制，(5) 在 MUI 版本间迁移或自定义组件行为。
---

# MUI Helper

## 什么时候使用这个 Skill

当以下场景时，自动触发此 Skill：

1. 创建或修改使用 Material-UI 的 UI 组件
2. 解决 MUI 组件实现问题
3. 查询 MUI 组件属性和 API
4. 实现 MUI 布局和主题定制
5. 在 MUI 版本间迁移或自定义组件行为

## 使用前必须查阅文档

### 重要提醒
**在使用任何 MUI 组件或功能前，必须先查阅 [docs.md](references/docs.md) 文档，找到对应组件或主题的具体 URL，仔细阅读官方文档后才能开始开发。**

### 为什么必须查阅文档
1. 每个 MUI 组件都有独特的 API 和属性
2. 官方文档包含正确的使用示例和最佳实践
3. 避免常见的错误用法和性能问题
4. 确保代码符合 MUI 的设计规范

### 查阅文档的步骤

#### 第一步：浏览 docs.md
参考文档按类别组织了所有 MUI 组件和功能：
- Components：所有组件列表
- Customization：主题定制相关
- Guides：使用指南
- Integrations：框架集成
- Migration：版本迁移

#### 第二步：找到具体的 URL
在 docs.md 中找到你需要的组件或功能，例如：
- `React Button component` → `https://mui.com/material-ui/react-button.md`
- `Dark mode` → `https://mui.com/material-ui/customization/dark-mode.md`
- `Next.js integration` → `https://mui.com/material-ui/integrations/nextjs.md`

#### 第三步：获取具体 URL 并阅读
使用 `webfetch` 工具获取文档内容，仔细阅读：
- 组件的 Props 和 API
- 示例代码
- 注意事项和限制
- 常见问题

#### 第四步：基于文档开发
确保完全理解文档内容后，再进行开发。

## 查阅文档示例

### 场景 1：使用 Button 组件
1. 在 docs.md 中找到 `React Button component`
2. 获取 URL：`https://mui.com/material-ui/react-button.md`
3. 使用 `webfetch` 获取文档内容
4. 阅读 Props 说明（variant, color, size, disabled 等）
5. 查看示例代码
6. 根据文档正确使用组件

### 场景 2：自定义主题
1. 在 docs.md 中找到 `Theming`
2. 获取 URL：`https://mui.com/material-ui/customization/theming.md`
3. 使用 `webfetch` 获取文档内容
4. 阅读 `createTheme` 的配置选项
5. 了解如何定义 palette, typography 等
6. 根据文档创建主题

### 场景 3：解决组件问题
1. 在 docs.md 中找到相关组件文档
2. 获取 URL 并查阅
3. 检查常见问题部分
4. 查看是否有 API 变更或废弃警告
5. 参考官方建议的解决方案

## 外部资源

- [官方文档](https://mui.com/material-ui/)
- [组件 API 搜索](https://mui.com/material-ui/api/all/)
- [示例项目](https://mui.com/material-ui/getting-started/example-projects.md)

## 参考文档

所有组件和功能的文档链接目录，参见 [docs.md](references/docs.md)
