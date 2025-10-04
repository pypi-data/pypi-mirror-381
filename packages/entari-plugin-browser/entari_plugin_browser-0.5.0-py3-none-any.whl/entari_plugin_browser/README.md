# entari-plugin-browser
Browser API service for Entari using Playwright

## 使用

### 导入

```python
from entari_plugin_browser import playwright_api, text2img


async def main():
    async with playwright_api.page() as page:
        await page.goto('https://www.baidu.com')
        await page.screenshot(path='baidu.png')
    
    img: bytes = await text2img('Hello, World!')
```

### 配置

在你的 Entari 配置文件中如下配置：(以 `entari.yml` 为例)

```yaml
plugins:
  browser:
    browser_type: chromium
    channel: chrome
    headless: true
    # ...
    # 更多配置请参考 Playwright 文档，详见 <https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch>
```

## HTMLRenderer

除了内置提供的 `text2img` 和 `md2img` 方法外，你还可以使用 `HTMLRenderer` 等来自定义渲染器。

```python
from entari_plugin_browser import HTMLRenderer, convert_md, PageOption, ScreenshotOption

md = """\
<div align="center">

# entari-plugin-browser

*Browser API service for Entari using Playwright*

</div>

## 使用

### 导入

from entari_plugin_browser import playwright_api, text2img


async def main():
    async with playwright_api.page() as page:
        await page.goto('https://www.baidu.com')
        await page.screenshot(path='baidu.png')
    
    img: bytes = await text2img('Hello, World!')
"""

async def function():
    image_bytes: bytes = await HTMLRenderer().render(
        convert_md(md),
        extra_page_option=PageOption(viewport={"width": 840, "height": 10}, device_scale_factor=1.5),
        extra_screenshot_option=ScreenshotOption(type="jpeg", quality=80, scale="device"),
    )
```

## 模板转图片（可选依赖 jinja2）

如需将 Jinja2 模板渲染为 HTML 并输出图片，安装可选依赖：

```bash
pip install "entari-plugin-browser[jinja2]"
```

示例：

```python
from entari_plugin_browser import template2img


async def main():
    text_list = ["1", "2", "3", "4"]
    template_path = "path/to/templates"
    template_name = "example.html"
    
    img: bytes = await template2img(
        template_path=template_path,
        template_name=template_name,
        templates={"text_list": text_list},
    )
```

说明：默认启用 HTML 自动转义，如需插入已转义 HTML，请在模板中使用 `|safe` 过滤器。
