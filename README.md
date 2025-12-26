# 鼠标录制软件

简要说明：这是一个示例 Python 项目，用于演示如何录制鼠标事件并保存为 JSON（基于 `pynput`）。

## 快速开始

推荐使用 Poetry 来管理依赖与虚拟环境（已在 `pyproject.toml` 中声明依赖）。

### 使用 Poetry（推荐）

1. 安装 Poetry（如果尚未安装）：

- 官方安装方法（跨平台）：
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
- 或参考官方文档：https://python-poetry.org/docs/#installation

2. 在项目根目录安装依赖：
```bash
cd "D:\workspace\鼠标录制软件"
poetry install
```

3. 运行示例（通过 console script）：
```bash
poetry run mouse-recorder --seconds 5 --out mouse_events.json
```

4. 运行测试：
```bash
poetry run pytest
```

### 如果不使用 Poetry（可选）

1. 使用 venv：
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt  # 若需要，可先生成 requirements.txt
```

2. 运行示例：
```bash
python scripts/run_record.py --seconds 5 --out mouse_events.json
```

---

## 打包为 Windows 可执行文件（EXE）

推荐使用 PyInstaller 来生成单文件的 Windows 可执行程序。下面有两种方法：

1. 使用附带的 PowerShell 脚本（推荐在 Windows 上运行）：

```powershell
# 在项目根目录下运行
.\.\scripts\build_exe.ps1
# 或者指定名称
.\.\scripts\build_exe.ps1 -Name mouse-recorder
```

脚本会优先使用 `poetry run pyinstaller`（如果你安装并使用 Poetry），否则将直接调用系统上的 `pyinstaller`。生成的 exe 位于 `dist\mouse-recorder.exe`。

2. 手动使用 PyInstaller：

```bash
# 安装 pyinstaller
poetry run pip install pyinstaller  # 或 python -m pip install pyinstaller

# 直接构建
poetry run pyinstaller --onefile --name mouse-recorder src/mouse_recorder/cli.py
```

注意：Windows 的防病毒软件有时会误报打包后的可执行文件；如需在 CI 上自动打包，请参考提供的 GitHub Actions workflow（`.github/workflows/build_windows_exe.yml`），该 workflow 会在 `windows-latest` runner 上构建 exe 并把 `dist/mouse-recorder.exe` 上传为 workflow artifact。

## 贡献

- 请先运行 `poetry install`，然后运行 `poetry run pytest` 来验证修改不会破坏现有行为。

## 许可

本项目使用 MIT 许可证.