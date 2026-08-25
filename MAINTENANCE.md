# 维护说明

当前版本：`V4.29.5`。

每次更新 `SKILL.md`、参考资料、schema、脚本、测试或 UI 元数据时，都必须递增版本、更新 `agents/openai.yaml` 的 `display_name`，并在 `CHANGELOG.md` 记录变更。展示名固定为 `GM 多平台商业文案创作 V版本号`。

提交前运行适用的静态验证和回归测试；行为模型测试未运行时必须如实记录，不能以静态检查替代。

所有文本文件以 UTF-8（无 BOM）保存；Windows 上的 Python 校验必须启用 UTF-8 模式，避免系统默认 GBK 造成误判。
