# 鼠标录制软件

简要说明：这是一个示例 Python 项目，用于演示如何录制鼠标事件并保存为 JSON（基于 `pynput`）。

## 快速开始

1. 安装依赖（推荐使用 Poetry）：

```bash
poetry install
```

2. 运行示例录制（记录 5 秒）：

```bash
python scripts/run_record.py --seconds 5 --out mouse_events.json
```

3. 运行测试：

```bash
poetry run pytest
```

## 许可

本项目使用 MIT 许可证。