import pygame
import pygame.gfxdraw
import time
import threading
import win32gui
import win32con
import win32api
import ctypes
from ctypes import wintypes
import os
import sys
from typing import Dict, List, Tuple, Any, Optional, Callable

# 高DPI处理
try:
    # 告诉Windows我们处理DPI缩放
    ctypes.windll.user32.SetProcessDPIAware()
except:
    pass

class PyHackGUI:
    def __init__(self, title: str = "PyHackGUI"):
        """初始化PyHackGUI，处理高DPI缩放"""
        # 初始化pygame
        pygame.init()

        # 获取真实屏幕尺寸（不考虑DPI缩放）
        self.screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        self.screen_height = ctypes.windll.user32.GetSystemMetrics(1)

        # 获取DPI缩放因子
        self.dpi_scale = self.get_dpi_scale()
        print(f"DPI缩放因子: {self.dpi_scale}")

        # 创建无边框窗口
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                             pygame.NOFRAME | pygame.SRCALPHA)

        # 设置窗口属性
        hwnd = pygame.display.get_wm_info()["window"]
        styles = (win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT |
                 win32con.WS_EX_TOPMOST | win32con.WS_EX_NOACTIVATE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                             win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60

        # 双缓冲表面
        self.buffer_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

        # 字体系统 - 修复高DPI和中文显示
        self.fonts: Dict[str, Dict[int, pygame.font.Font]] = {}
        self.selected_font_path: Optional[str] = None
        self.load_fonts()

        # 图片缓存
        self._images: Dict[str, pygame.Surface] = {}

        # 文本输入管理
        self._text_inputs: Dict[str, Dict] = {}

        # GUI状态
        self.mouse_pos = (0, 0)
        # 全局鼠标输入（覆盖层穿透时，使用全局GetAsyncKeyState检测）
        self.lmb_down = False
        self.prev_lmb_down = False
        self.lmb_clicked = False
        self.lmb_released = False
        self.rmb_down = False
        self.prev_rmb_down = False
        self.rmb_clicked = False
        self.rmb_released = False
        self.mmb_down = False
        self.prev_mmb_down = False
        self.mmb_clicked = False
        self.mmb_released = False
        self.active_window = None
        self.hovered_item = None

        # 样式配置
        self.style = {
            'window': {'bg_color': (30, 30, 40, 220), 'border_color': (80, 80, 100, 255), 'border_size': 2},
            'button': {'bg_color': (60, 60, 80, 255), 'hover_color': (80, 80, 100, 255), 'text_color': (255, 255, 255, 255)},
            'slider': {'bg_color': (50, 50, 70, 255), 'fill_color': (0, 120, 255, 255), 'handle_color': (200, 200, 200, 255)},
            'checkbox': {'bg_color': (50, 50, 70, 255), 'check_color': (0, 200, 100, 255), 'text_color': (255, 255, 255, 255)},
            'toggle': {'on_color': (0, 200, 100, 255), 'off_color': (90, 90, 110, 255), 'knob_color': (240, 240, 240, 255)},
            'radio': {'outer_color': (200, 200, 200, 255), 'inner_color': (0, 200, 100, 255), 'text_color': (255, 255, 255, 255)},
            'combo': {'bg_color': (60, 60, 80, 255), 'hover_color': (80, 80, 100, 255), 'text_color': (255, 255, 255, 255)},
            'panel': {'bg_color': (25, 25, 35, 220), 'title_color': (40, 40, 55, 240), 'title_text': (255, 255, 255, 230), 'border_color': (80, 80, 100, 255)},
            'keybind': {'bg_color': (60, 60, 80, 255), 'capturing_color': (120, 60, 60, 255), 'text_color': (255, 255, 255, 255)},
            'text': {'color': (255, 255, 255, 255)},
            'progress': {'bg_color': (50, 50, 70, 255), 'fill_color': (0, 200, 100, 255)},
        }

        # GUI元素存储
        self.windows: Dict[str, Dict] = {}
        self.buttons: Dict[str, Dict] = {}
        self.sliders: Dict[str, Dict] = {}
        self.checkboxes: Dict[str, Dict] = {}
        self.labels: Dict[str, Dict] = {}
        self.toggles: Dict[str, Dict] = {}
        self.radio_groups: Dict[str, Dict] = {}
        self.combos: Dict[str, Dict] = {}
        self.panels: Dict[str, Dict] = {}
        self.color_pickers: Dict[str, Dict] = {}
        self.keybinds: Dict[str, Dict] = {}

        # 拖拽状态
        self.dragging_panel = None
        self.drag_offset = (0, 0)

        # 热键捕获状态
        self.capturing_key = None
        self.captured_keys = set()

        # 下拉菜单状态
        self.active_combo = None
        # 需要后绘制的覆盖层（例如下拉列表），按优先级最后绘制，避免被其他控件遮挡
        self.overlay_draws = []

        # 性能监控
        self.frame_count = 0
        self.last_time = time.time()
        self.fps_text = "FPS: 0"



        # 启动渲染线程
        self.render_thread = threading.Thread(target=self.render_loop)
        self.render_thread.daemon = True
        self.render_thread.start()

    def get_dpi_scale(self) -> float:
        """获取系统DPI缩放因子"""
        try:
            # 获取主显示器的DPI
            hdc = ctypes.windll.user32.GetDC(0)
            dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return dpi / 96.0
        except:
            return 1.0

    def scale_value(self, value: int) -> int:
        """根据DPI缩放值"""
        return int(value * self.dpi_scale)

    def update_input(self):
        """更新全局鼠标位置与按键（穿透窗口场景）"""
        # 光标位置（全局）
        try:
            x, y = win32api.GetCursorPos()
            self.mouse_pos = (x, y)
        except Exception:
            try:
                self.mouse_pos = pygame.mouse.get_pos()
            except Exception:
                pass

        def is_down(vk: int) -> bool:
            try:
                return (win32api.GetAsyncKeyState(vk) & 0x8000) != 0
            except Exception:
                # 退回到pygame（在本窗口聚焦时可用）
                try:
                    pressed = pygame.mouse.get_pressed()
                    if vk == 0x01:
                        return pressed[0]
                    if vk == 0x02:
                        return pressed[2]
                    if vk == 0x04:
                        return pressed[1]
                except Exception:
                    return False
                return False

        # 记录旧状态以产生边沿事件
        prev_l = self.lmb_down
        prev_r = self.rmb_down
        prev_m = self.mmb_down

        new_l = is_down(0x01)
        self.lmb_clicked = new_l and not prev_l
        self.lmb_released = (not new_l) and prev_l
        self.lmb_down = new_l

        new_r = is_down(0x02)
        self.rmb_clicked = new_r and not prev_r
        self.rmb_released = (not new_r) and prev_r
        self.rmb_down = new_r

        new_m = is_down(0x04)
        self.mmb_clicked = new_m and not prev_m
        self.mmb_released = (not new_m) and prev_m
        self.mmb_down = new_m

        # 兼容旧字段
        self.mouse_pressed = self.lmb_down

        # 鼠标滚轮累计（每帧重置，正值=向上，负值=向下）
        self.wheel_y = 0
        try:
            for ev in pygame.event.get(pygame.MOUSEWHEEL):
                self.wheel_y += ev.y
        except Exception:
            self.wheel_y = 0

        # 处理键盘输入事件（仅用于文本输入控件）
        try:
            for ev in pygame.event.get([pygame.KEYDOWN, pygame.TEXTINPUT, pygame.KEYUP]):
                # TEXTINPUT 用于输入可打印字符（支持输入法），KEYDOWN 用于控制键和退格
                if ev.type == pygame.TEXTINPUT:
                    # 将输入字符分派给激活的文本输入控件（最后创建的或被聚焦的）
                    for name, state in self._text_inputs.items():
                        if state.get('focused'):
                            state['text'] += ev.text
                elif ev.type == pygame.KEYDOWN:
                    for name, state in self._text_inputs.items():
                        if not state.get('focused'):
                            continue
                        # 处理特殊按键
                        if ev.key == pygame.K_BACKSPACE:
                            state['text'] = state['text'][:-1]
                        elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                            # 提交/失去焦点
                            state['focused'] = False
                            if state.get('on_submit'):
                                try:
                                    state['on_submit'](state['text'])
                                except Exception:
                                    pass
                        elif ev.key == pygame.K_ESCAPE:
                            state['focused'] = False
                # KEYUP 不做特殊处理
        except Exception:
            pass

    def load_fonts(self):
        """加载字体系统，修复高DPI和中文显示"""
        # 初始化所选字体路径
        self.selected_font_path = None

        # 常见的中文字体路径
        font_paths = [
            "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
            "C:/Windows/Fonts/simhei.ttf",    # 黑体
            "C:/Windows/Fonts/simsun.ttc",    # 宋体
            "C:/Windows/Fonts/arialuni.ttf",  # Arial Unicode
        ]

        # 尝试加载中文字体（直接指定路径）
        loaded = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    base_size = self.scale_value(20)
                    font = pygame.font.Font(font_path, base_size)
                    self.fonts['chinese'] = {base_size: font}
                    self.selected_font_path = font_path
                    print(f"成功加载中文字体: {font_path}")
                    loaded = True
                    break
                except Exception as e:
                    print(f"字体加载失败 {font_path}: {e}")

        # 如果中文字体加载失败，尝试系统匹配
        if not loaded:
            try:
                candidates = [
                    "msyh", "Microsoft YaHei", "simhei", "simsun",
                    "arialunicode", "Arial Unicode MS", "Noto Sans CJK SC"
                ]
                matched = pygame.font.match_font(candidates)
                base_size = self.scale_value(20)
                if matched:
                    self.selected_font_path = matched
                    self.fonts['chinese'] = {base_size: pygame.font.Font(matched, base_size)}
                    print(f"使用系统匹配中文字体: {matched}")
                else:
                    # 退回到默认字体（可能不支持中文）
                    self.fonts['chinese'] = {base_size: pygame.font.Font(None, base_size)}
                    print("未找到中文字体，使用pygame默认字体（可能不支持中文）")
            except Exception as e:
                base_size = self.scale_value(20)
                self.fonts['chinese'] = {base_size: pygame.font.Font(None, base_size)}
                print(f"系统字体匹配失败，使用pygame默认字体: {e}")

    def get_font(self, name: str = 'chinese', size: Optional[int] = None) -> pygame.font.Font:
        """获取字体，自动处理DPI缩放"""
        if size is None:
            size = self.scale_value(20)
        else:
            size = self.scale_value(size)

        if name not in self.fonts:
            self.fonts[name] = {}
        if size in self.fonts[name]:
            return self.fonts[name][size]

        # 优先使用选中的中文字体路径创建不同尺寸
        try:
            if name == 'chinese' and self.selected_font_path:
                new_font = pygame.font.Font(self.selected_font_path, size)
                self.fonts[name][size] = new_font
                return new_font
        except Exception as e:
            print(f"创建指定中文字体失败，将回退: {e}")

        # 再次尝试系统匹配一个可用中文字体
        try:
            matched = pygame.font.match_font([
                "msyh", "Microsoft YaHei", "simhei", "simsun",
                "arialunicode", "Arial Unicode MS", "Noto Sans CJK SC"
            ])
            if matched:
                new_font = pygame.font.Font(matched, size)
                self.fonts[name][size] = new_font
                return new_font
        except:
            pass

        # 最后回退到默认字体
        self.fonts[name][size] = pygame.font.Font(None, size)
        return self.fonts[name][size]

    def draw_text(self, text: str, pos: Tuple[int, int], color: Optional[Tuple[int, int, int, int]] = None,
                 font_name: str = 'chinese', size: Optional[int] = None, antialias: bool = True):
        """绘制文本（修复高DPI和中文显示）"""
        color = color or self.style['text']['color']
        font = self.get_font(font_name, size)

        try:
            # 使用font.render的第二个参数来启用抗锯齿
            text_surface = font.render(text, antialias, color)
            # 应用DPI缩放到位置
            scaled_pos = (self.scale_value(pos[0]), self.scale_value(pos[1]))
            self.buffer_surface.blit(text_surface, scaled_pos)
        except Exception as e:
            print(f"文本渲染错误: {e}")

    def draw_text_outline(self, text: str, pos: Tuple[int, int], color: Tuple[int, int, int, int] = (255,255,255,255), outline_color: Tuple[int, int, int, int] = (0,0,0,255), outline_width: int = 1, font_name: str = 'chinese', size: Optional[int] = None, antialias: bool = True):
        font = self.get_font(font_name, size)
        # 先渲染正文表面
        try:
            base = font.render(text, antialias, color)
            ox = self.scale_value(pos[0])
            oy = self.scale_value(pos[1])
            # 描边
            for dx in range(-outline_width, outline_width+1):
                for dy in range(-outline_width, outline_width+1):
                    if dx == 0 and dy == 0:
                        continue
                    outline_surf = font.render(text, antialias, outline_color)
                    self.buffer_surface.blit(outline_surf, (ox + dx, oy + dy))
            # 正文
            self.buffer_surface.blit(base, (ox, oy))
        except Exception as e:
            print(f"文本描边渲染错误: {e}")

    def load_image(self, key: str, path: str) -> bool:


        
        """加载图片并缓存，key 为自定义标识"""
        try:
            if not os.path.exists(path):
                return False
            img = pygame.image.load(path).convert_alpha()
            self._images[key] = img
            return True
        except Exception as e:
            print(f"加载图片失败: {e}")
            return False

    def draw_image(self, key: str, pos: Tuple[int, int], size: Optional[Tuple[int, int]] = None, rotate: float = 0.0, alpha: Optional[int] = None):
        """绘制已缓存的图片；如果 size 提供则缩放。pos 为左上角（未缩放的逻辑坐标）。"""
        if key not in self._images:
            return
        try:
            img = self._images[key]
            w, h = img.get_size()
            if size:
                sw, sh = self.scale_value(size[0]), self.scale_value(size[1])
                img_to_draw = pygame.transform.smoothscale(img, (sw, sh))
            else:
                img_to_draw = img
            if rotate and rotate % 360 != 0:
                img_to_draw = pygame.transform.rotate(img_to_draw, rotate)
            if alpha is not None:
                img_to_draw = img_to_draw.copy()
                img_to_draw.set_alpha(alpha)
            self.buffer_surface.blit(img_to_draw, (self.scale_value(pos[0]), self.scale_value(pos[1])))
        except Exception as e:
            print(f"绘制图片失败: {e}")

    def _ensure_text_input(self, name: str):
        if name not in self._text_inputs:
            self._text_inputs[name] = {'text': '', 'focused': False, 'rect': None, 'on_submit': None, 'placeholder': ''}

    def text_input(self, name: str, pos: Tuple[int, int], size: Tuple[int, int], placeholder: str = '', initial: str = '', on_submit: Optional[Callable[[str], None]] = None) -> str:
        """渲染并交互一个文本输入框。返回当前文本值。"""
        self._ensure_text_input(name)
        state = self._text_inputs[name]
        state['placeholder'] = placeholder
        if 'text' not in state or state['text'] == '':
            if initial:
                state['text'] = initial

        x, y = self.scale_value(pos[0]), self.scale_value(pos[1])
        w, h = self.scale_value(size[0]), self.scale_value(size[1])
        rect = pygame.Rect(x, y, w, h)
        state['rect'] = rect

        # 背景与边框
        pygame.draw.rect(self.buffer_surface, (40, 40, 50, 220), rect, border_radius=self.scale_value(4))
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], rect, self.scale_value(1), border_radius=self.scale_value(4))

        # 点击聚焦
        if rect.collidepoint(self.mouse_pos) and self.lmb_clicked:
            # 取消其他输入的焦点
            for k in self._text_inputs:
                self._text_inputs[k]['focused'] = False
            state['focused'] = True

        # 光标和文本绘制
        display_text = state.get('text', '')
        if display_text == '' and not state.get('focused') and placeholder:
            # 占位文本
            font = self.get_font('chinese', 16)
            surf = font.render(placeholder, True, (160, 160, 160, 200))
            self.buffer_surface.blit(surf, (x + self.scale_value(6), y + (h - surf.get_height()) // 2))
        else:
            font = self.get_font('chinese', 16)
            surf = font.render(display_text, True, self.style['text']['color'])
            self.buffer_surface.blit(surf, (x + self.scale_value(6), y + (h - surf.get_height()) // 2))

        # 光标（如果聚焦）
        if state.get('focused'):
            try:
                cursor_x = x + self.scale_value(6) + surf.get_width() + 2
                cursor_y1 = y + self.scale_value(6)
                cursor_y2 = y + h - self.scale_value(6)
                # 简单闪烁
                if int(time.time() * 2) % 2 == 0:
                    pygame.draw.line(self.buffer_surface, (255, 255, 255, 255), (cursor_x, cursor_y1), (cursor_x, cursor_y2), self.scale_value(1))
            except Exception:
                pass

        # 回调保存
        state['on_submit'] = on_submit

        self._text_inputs[name] = state
        return state.get('text', '')

    def button(self, name: str, pos: Tuple[int, int], size: Tuple[int, int], text: str) -> bool:
        """创建一个按钮"""
        # 应用DPI缩放
        scaled_pos = (self.scale_value(pos[0]), self.scale_value(pos[1]))
        scaled_size = (self.scale_value(size[0]), self.scale_value(size[1]))

        rect = pygame.Rect(scaled_pos[0], scaled_pos[1], scaled_size[0], scaled_size[1])
        hover = rect.collidepoint(self.mouse_pos)
        clicked = False

        # 绘制按钮
        color = self.style['button']['hover_color'] if hover else self.style['button']['bg_color']
        pygame.draw.rect(self.buffer_surface, color, rect, border_radius=self.scale_value(5))
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], rect,
                        self.scale_value(1), border_radius=self.scale_value(5))

        # 绘制文本
        font = self.get_font('chinese', 16)
        text_surf = font.render(text, True, self.style['button']['text_color'])
        text_rect = text_surf.get_rect(center=rect.center)
        self.buffer_surface.blit(text_surf, text_rect)

        # 检测点击（按下沿触发，支持穿透）
        if hover and self.lmb_clicked:
            clicked = True

        self.buttons[name] = {'rect': rect, 'hover': hover, 'clicked': clicked}
        return clicked

    def toggle(self, name: str, pos: Tuple[int, int], checked: bool, text: str = "") -> bool:
        """开关（Switch/Toggle）"""
        w, h = self.scale_value(40), self.scale_value(22)
        radius = h // 2
        x, y = self.scale_value(pos[0]), self.scale_value(pos[1])
        rect = pygame.Rect(x, y, w, h)
        hover = rect.collidepoint(self.mouse_pos)

        # 背景
        bg = self.style['toggle']['on_color'] if checked else self.style['toggle']['off_color']
        pygame.draw.rect(self.buffer_surface, bg, rect, border_radius=radius)
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], rect, self.scale_value(1), border_radius=radius)

        # 圆钮
        knob_r = radius - self.scale_value(2)
        knob_x = x + (w - radius) if checked else x
        knob_center = (knob_x + radius, y + radius)
        pygame.gfxdraw.filled_circle(self.buffer_surface, knob_center[0], knob_center[1], knob_r, self.style['toggle']['knob_color'])
        pygame.gfxdraw.aacircle(self.buffer_surface, knob_center[0], knob_center[1], knob_r, self.style['toggle']['knob_color'])

        # 文本
        if text:
            self.draw_text(text, (pos[0] + 50, pos[1] - 2), size=16)

        if hover and self.lmb_clicked:
            checked = not checked

        self.toggles[name] = {'rect': rect, 'checked': checked, 'hover': hover}
        return checked

    def radio_group(self, name: str, options: List[str], selected: str, pos: Tuple[int, int], item_spacing: int = 26) -> str:
        """单选组（垂直）"""
        x0, y0 = pos
        circle_r = self.scale_value(8)
        for i, opt in enumerate(options):
            y = y0 + i * item_spacing
            cx, cy = self.scale_value(x0), self.scale_value(y)
            # 外圈
            pygame.gfxdraw.aacircle(self.buffer_surface, cx, cy, circle_r, self.style['radio']['outer_color'])
            pygame.gfxdraw.aacircle(self.buffer_surface, cx, cy, circle_r-1, self.style['radio']['outer_color'])
            # 选中内点
            item_rect = pygame.Rect(cx - circle_r, cy - circle_r, circle_r*2, circle_r*2)
            hover = item_rect.collidepoint(self.mouse_pos)
            if selected == opt:
                pygame.gfxdraw.filled_circle(self.buffer_surface, cx, cy, circle_r-3, self.style['radio']['inner_color'])
            # 文本
            self.draw_text(opt, (x0 + 20, y - 8), size=16)
            # 点击
            if (hover or pygame.Rect(self.scale_value(x0 + 20), self.scale_value(y - 10), self.scale_value(150), self.scale_value(20)).collidepoint(self.mouse_pos)) and self.lmb_clicked:
                selected = opt
        self.radio_groups[name] = {'selected': selected, 'options': options}
        return selected
    def combo(self, name: str, pos: Tuple[int, int], width: int, items: List[str], selected_index: int) -> int:
        """下拉框 Combo，使用 self.active_combo 追踪展开状态"""
        x, y = self.scale_value(pos[0]), self.scale_value(pos[1])
        h = self.scale_value(24)
        w = self.scale_value(width)
        header_rect = pygame.Rect(x, y, w, h)
        hover_header = header_rect.collidepoint(self.mouse_pos)

        # 头部背景
        bg = self.style['combo']['hover_color'] if hover_header else self.style['combo']['bg_color']
        pygame.draw.rect(self.buffer_surface, bg, header_rect, border_radius=self.scale_value(4))
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], header_rect, self.scale_value(1), border_radius=self.scale_value(4))

        # 文字
        current_text = items[selected_index] if 0 <= selected_index < len(items) else ""
        self.draw_text(current_text, (pos[0] + 6, pos[1] + 3), size=16)

        # 小三角
        tri_x = x + w - self.scale_value(14)
        tri_y = y + h // 2
        pygame.draw.polygon(self.buffer_surface, (220, 220, 220, 255), [(tri_x-5, tri_y-3), (tri_x+5, tri_y-3), (tri_x, tri_y+3)])

        opened = (self.active_combo == name)
        if hover_header and self.lmb_clicked:
            # 切换展开
            self.active_combo = None if opened else name
            opened = not opened

        # 鼠标滚轮：未展开时在头部滚动也可切换选项
        if hover_header and getattr(self, 'wheel_y', 0) != 0 and len(items) > 0:
            selected_index = max(0, min(len(items)-1, selected_index - self.wheel_y))

        # 展开条目
        item_rects = []
        if opened:
            list_height = h * max(1, len(items))
            list_rect = pygame.Rect(x, y + h + self.scale_value(2), w, list_height)

            # 鼠标滚轮：在列表上滚动切换选项
            if getattr(self, 'wheel_y', 0) != 0 and list_rect.collidepoint(self.mouse_pos) and len(items) > 0:
                selected_index = max(0, min(len(items)-1, selected_index - self.wheel_y))

            # 先正常绘制一次（保证交互逻辑不变）
            pygame.draw.rect(self.buffer_surface, self.style['combo']['bg_color'], list_rect, border_radius=self.scale_value(4))
            pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], list_rect, self.scale_value(1), border_radius=self.scale_value(4))
            for i, it in enumerate(items):
                ir = pygame.Rect(x, y + h + self.scale_value(2) + i * h, w, h)
                hover = ir.collidepoint(self.mouse_pos)
                if hover:
                    pygame.draw.rect(self.buffer_surface, self.style['combo']['hover_color'], ir)
                self.draw_text(it, (pos[0] + 6, pos[1] + 3 + (i+1) * 24 + 2), size=16)
                item_rects.append(ir)
                if hover and self.lmb_clicked:
                    selected_index = i
                    self.active_combo = None
                    opened = False

            # 点击外部收起
            if self.lmb_clicked:
                outside = (not header_rect.collidepoint(self.mouse_pos)) and all(not r.collidepoint(self.mouse_pos) for r in item_rects)
                if outside:
                    self.active_combo = None

            # 叠加一次后绘制，确保下拉层级位于最上方
            def _draw_combo_overlay(x=x, y=y, h=h, w=w, pos=pos, items=list(items)):
                _list_height = h * max(1, len(items))
                _list_rect = pygame.Rect(x, y + h + self.scale_value(2), w, _list_height)
                pygame.draw.rect(self.buffer_surface, self.style['combo']['bg_color'], _list_rect, border_radius=self.scale_value(4))
                pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], _list_rect, self.scale_value(1), border_radius=self.scale_value(4))
                for i, it in enumerate(items):
                    _ir = pygame.Rect(x, y + h + self.scale_value(2) + i * h, w, h)
                    if _ir.collidepoint(self.mouse_pos):
                        pygame.draw.rect(self.buffer_surface, self.style['combo']['hover_color'], _ir)
                    self.draw_text(it, (pos[0] + 6, pos[1] + 3 + (i+1) * 24 + 2), size=16)
            # active_combo 优先级最高
            self.overlay_draws.append((10, _draw_combo_overlay))

        self.combos[name] = {'rect': header_rect, 'opened': opened, 'selected': selected_index}
        return selected_index

    def color_picker(self, name: str, pos: Tuple[int, int], color: Tuple[int, int, int, int] = (255,0,0,255), with_alpha: bool = False) -> Tuple[int, int, int, int]:
        state = self.color_pickers.get(name, {'open': False})

        # 初始化颜色状态（如果不存在）
        if 'r' not in state:
            state['r'], state['g'], state['b'], state['a'] = color

        x, y = self.scale_value(pos[0]), self.scale_value(pos[1])
        box_rect = pygame.Rect(x, y, self.scale_value(30), self.scale_value(18))

        # 使用状态中的颜色绘制颜色框
        current_color = (state['r'], state['g'], state['b'], state['a'])
        pygame.draw.rect(self.buffer_surface, current_color, box_rect, border_radius=self.scale_value(3))
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], box_rect, self.scale_value(1), border_radius=self.scale_value(3))
        self.draw_text("颜色", (pos[0] + 36, pos[1] - 2), size=16)

        if box_rect.collidepoint(self.mouse_pos) and self.lmb_clicked:
            state['open'] = not state.get('open', False)
        if state.get('open', False):
            panel_w = self.scale_value(220)
            panel_h = self.scale_value(110 if with_alpha else 90)
            panel_rect = pygame.Rect(x, y + self.scale_value(22), panel_w, panel_h)

            # 使用覆盖层绘制颜色选择器面板
            def _draw_color_picker_overlay():
                # 绘制面板背景
                pygame.draw.rect(self.buffer_surface, self.style['panel']['bg_color'], panel_rect, border_radius=self.scale_value(6))
                pygame.draw.rect(self.buffer_surface, self.style['panel']['border_color'], panel_rect, self.scale_value(1), border_radius=self.scale_value(6))

                # 三条/四条滑条（在覆盖层中绘制和处理）
                state['r'] = int(self.slider_float(f"{name}_r", (pos[0] + 8, pos[1] + 28), (180, 16), float(state['r']), 0.0, 255.0, "R: %.0f"))
                state['g'] = int(self.slider_float(f"{name}_g", (pos[0] + 8, pos[1] + 50), (180, 16), float(state['g']), 0.0, 255.0, "G: %.0f"))
                state['b'] = int(self.slider_float(f"{name}_b", (pos[0] + 8, pos[1] + 72), (180, 16), float(state['b']), 0.0, 255.0, "B: %.0f"))
                if with_alpha:
                    state['a'] = int(self.slider_float(f"{name}_a", (pos[0] + 8, pos[1] + 94), (180, 16), float(state['a']), 0.0, 255.0, "A: %.0f"))

                # 预览颜色
                prev_rect = pygame.Rect(panel_rect.right - self.scale_value(36), panel_rect.y + self.scale_value(10), self.scale_value(26), self.scale_value(26))
                pygame.draw.rect(self.buffer_surface, (state['r'], state['g'], state['b'], state['a']), prev_rect, border_radius=self.scale_value(4))
                pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], prev_rect, self.scale_value(1), border_radius=self.scale_value(4))

            # 添加到覆盖层绘制列表，优先级为15（比下拉框高）
            self.overlay_draws.append((15, _draw_color_picker_overlay))

            # 外部点击则关闭
            if self.lmb_clicked and not (panel_rect.collidepoint(self.mouse_pos) or box_rect.collidepoint(self.mouse_pos)):
                state['open'] = False

        # 返回当前状态中的颜色
        result_color = (max(0, min(255, state['r'])), max(0, min(255, state['g'])), max(0, min(255, state['b'])), max(0, min(255, state['a'])))
        self.color_pickers[name] = state
        return result_color

    def vk_to_name(self, vk: Optional[int]) -> str:
        names = {
            0x01: 'LMB', 0x02: 'RMB', 0x04: 'MMB',
            0x08: 'BACK', 0x09: 'TAB', 0x0D: 'ENTER', 0x10: 'SHIFT', 0x11: 'CTRL', 0x12: 'ALT', 0x14: 'CAPS', 0x1B: 'ESC',
            0x20: 'SPACE', 0x21: 'PGUP', 0x22: 'PGDN', 0x23: 'END', 0x24: 'HOME', 0x25: 'LEFT', 0x26: 'UP', 0x27: 'RIGHT', 0x28: 'DOWN',
            0x2C: 'PRTSC', 0x2D: 'INS', 0x2E: 'DEL',
        }
        if vk is None:
            return 'None'
        if 0x30 <= vk <= 0x39:
            return chr(vk)
        if 0x41 <= vk <= 0x5A:
            return chr(vk)
        if 0x70 <= vk <= 0x7B:
            return f'F{vk-0x6F}'
        return names.get(vk, f'VK_{vk:02X}')

    def keybind(self, name: str, pos: Tuple[int, int], width: int, vk_code: Optional[int]) -> Optional[int]:
        x, y = self.scale_value(pos[0]), self.scale_value(pos[1])
        w, h = self.scale_value(width), self.scale_value(24)
        rect = pygame.Rect(x, y, w, h)
        capturing = (self.capturing_key == name)

        bg = self.style['keybind']['capturing_color'] if capturing else self.style['keybind']['bg_color']
        pygame.draw.rect(self.buffer_surface, bg, rect, border_radius=self.scale_value(4))
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], rect, self.scale_value(1), border_radius=self.scale_value(4))
        label = 'Press a key...' if capturing else self.vk_to_name(vk_code)
        self.draw_text(label, (pos[0] + 6, pos[1] + 3), size=16)


        if rect.collidepoint(self.mouse_pos) and self.lmb_clicked:
            self.capturing_key = None if capturing else name
            capturing = not capturing
        if capturing:
            if (win32api.GetAsyncKeyState(0x1B) & 0x8000) != 0:
                vk_code = None
                self.capturing_key = None
            else:
                for vk in list(range(0x08, 0x91)) + list(range(0xA0, 0xFE)):
                    if (win32api.GetAsyncKeyState(vk) & 0x8000) != 0:
                        vk_code = vk
                        self.capturing_key = None
                        break

        self.keybinds[name] = {'rect': rect, 'vk': vk_code, 'capturing': capturing}
        return vk_code



    def slider_float(self, name: str, pos: Tuple[int, int], size: Tuple[int, int],
                    value: float, min_val: float, max_val: float, format: str = "%.1f") -> float:
        """创建一个浮点数滑块"""
        scaled_pos = (self.scale_value(pos[0]), self.scale_value(pos[1]))
        scaled_size = (self.scale_value(size[0]), self.scale_value(size[1]))

        rect = pygame.Rect(scaled_pos[0], scaled_pos[1], scaled_size[0], scaled_size[1])
        handle_width = self.scale_value(10)
        handle_pos = int((value - min_val) / (max_val - min_val) * (scaled_size[0] - handle_width))

        # 绘制滑块背景
        pygame.draw.rect(self.buffer_surface, self.style['slider']['bg_color'], rect,
                        border_radius=self.scale_value(3))

        # 绘制填充
        fill_rect = pygame.Rect(scaled_pos[0], scaled_pos[1], handle_pos + handle_width//2, scaled_size[1])
        pygame.draw.rect(self.buffer_surface, self.style['slider']['fill_color'], fill_rect,
                        border_radius=self.scale_value(3))

        # 绘制手柄
        handle_rect = pygame.Rect(scaled_pos[0] + handle_pos, scaled_pos[1] - self.scale_value(2),
                                handle_width, scaled_size[1] + self.scale_value(4))
        pygame.draw.rect(self.buffer_surface, self.style['slider']['handle_color'], handle_rect,
                        border_radius=self.scale_value(3))

        # 绘制数值
        value_text = format % value
        self.draw_text(value_text, (pos[0] + size[0] + 10, pos[1]), size=14)

        # 交互（按住左键拖动）
        hover = rect.collidepoint(self.mouse_pos)
        if hover and self.lmb_down:
            rel_x = self.mouse_pos[0] - scaled_pos[0]
            new_value = min_val + (rel_x / scaled_size[0]) * (max_val - min_val)
            value = max(min_val, min(max_val, new_value))

        self.sliders[name] = {'rect': rect, 'value': value, 'hover': hover}
        return value

    def checkbox(self, name: str, pos: Tuple[int, int], checked: bool, text: str) -> bool:
        """创建一个复选框"""
        box_size = self.scale_value(20)
        scaled_pos = (self.scale_value(pos[0]), self.scale_value(pos[1]))

        box_rect = pygame.Rect(scaled_pos[0], scaled_pos[1], box_size, box_size)
        text_pos = (pos[0] + 30, pos[1])  # 文本位置不缩放，因为draw_text内部会处理

        # 绘制复选框
        pygame.draw.rect(self.buffer_surface, self.style['checkbox']['bg_color'], box_rect,
                        border_radius=self.scale_value(3))
        pygame.draw.rect(self.buffer_surface, self.style['window']['border_color'], box_rect,
                        self.scale_value(1), border_radius=self.scale_value(3))

        if checked:
            check_rect = pygame.Rect(scaled_pos[0] + self.scale_value(5), scaled_pos[1] + self.scale_value(5),
                                   box_size - self.scale_value(10), box_size - self.scale_value(10))
            pygame.draw.rect(self.buffer_surface, self.style['checkbox']['check_color'], check_rect,
                            border_radius=self.scale_value(2))

        # 绘制文本
        self.draw_text(text, text_pos, size=16)

        # 交互（按下沿触发）
        hover = box_rect.collidepoint(self.mouse_pos)
        if hover and self.lmb_clicked:
            checked = not checked

        self.checkboxes[name] = {'rect': box_rect, 'checked': checked, 'hover': hover}
        return checked

    def panel(self, name: str, title: str, pos: Tuple[int, int], size: Tuple[int, int], movable: bool = True, closable: bool = True, minimizable: bool = True) -> Dict:
        """可拖拽面板容器，含标题栏/最小化/关闭按钮"""
        # 初始化/读取状态
        p = self.panels.get(name)
        if not p:
            p = {
                'rect': pygame.Rect(self.scale_value(pos[0]), self.scale_value(pos[1]), self.scale_value(size[0]), self.scale_value(size[1])),
                'minimized': False,
                'closed': False,
                'dragging': False,
            }
            self.panels[name] = p
        rect: pygame.Rect = p['rect']
        title_h = self.scale_value(26)
        title_rect = pygame.Rect(rect.x, rect.y, rect.w, title_h)

        if p.get('closed'):
            return p

        # 拖拽
        if movable:
            if not p['dragging'] and title_rect.collidepoint(self.mouse_pos) and self.lmb_clicked:
                self.dragging_panel = name
                self.drag_offset = (self.mouse_pos[0] - rect.x, self.mouse_pos[1] - rect.y)
                p['dragging'] = True
            if p['dragging'] and self.dragging_panel == name:
                if self.lmb_down:
                    new_x = self.mouse_pos[0] - self.drag_offset[0]
                    new_y = self.mouse_pos[1] - self.drag_offset[1]
                    rect.topleft = (new_x, new_y)
                if self.lmb_released:
                    p['dragging'] = False
                    self.dragging_panel = None

        # 背景与边框（最小化时仅绘制标题栏，不绘制整面板黑框）
        if not p.get('minimized', False):
            pygame.draw.rect(self.buffer_surface, self.style['panel']['bg_color'], rect, border_radius=self.scale_value(6))
            pygame.draw.rect(self.buffer_surface, self.style['panel']['border_color'], rect, self.scale_value(1), border_radius=self.scale_value(6))
        # 标题栏
        pygame.draw.rect(self.buffer_surface, self.style['panel']['title_color'], title_rect, border_radius=self.scale_value(6))
        # 最小化时给标题栏加边框，避免黑框残留
        if p.get('minimized', False):
            pygame.draw.rect(self.buffer_surface, self.style['panel']['border_color'], title_rect, self.scale_value(1), border_radius=self.scale_value(6))
        self.draw_text(title, (int(rect.x/ self.dpi_scale)+10, int(rect.y/ self.dpi_scale)+4), self.style['panel']['title_text'], size=16)

        # 标题栏按钮
        btn_w = self.scale_value(18)
        x_right = rect.right - self.scale_value(6)
        buttons = {}
        if minimizable:
            min_rect = pygame.Rect(x_right - btn_w*2, rect.y + (title_h - btn_w)//2, btn_w, btn_w)
            buttons['min'] = min_rect
            pygame.draw.rect(self.buffer_surface, (90, 90, 110, 255), min_rect, border_radius=self.scale_value(3))
            self.draw_text('-', (int(min_rect.x/ self.dpi_scale)+6, int(min_rect.y/ self.dpi_scale)-2), size=20)
        if closable:
            close_rect = pygame.Rect(x_right - btn_w, rect.y + (title_h - btn_w)//2, btn_w, btn_w)
            buttons['close'] = close_rect
            pygame.draw.rect(self.buffer_surface, (120, 70, 70, 255), close_rect, border_radius=self.scale_value(3))
            self.draw_text('x', (int(close_rect.x/ self.dpi_scale)+5, int(close_rect.y/ self.dpi_scale)+1), size=16)

        # 按钮点击
        if self.lmb_clicked:
            if 'min' in buttons and buttons['min'].collidepoint(self.mouse_pos):
                p['minimized'] = not p['minimized']
            if 'close' in buttons and buttons['close'].collidepoint(self.mouse_pos):
                p['closed'] = True

        # 内容区域
        content_rect = pygame.Rect(rect.x + self.scale_value(8), rect.y + title_h + self.scale_value(6), rect.w - self.scale_value(16), rect.h - title_h - self.scale_value(14))
        p['content_rect'] = content_rect
        p['title_rect'] = title_rect
        p['rect'] = rect
        p['visible'] = not p['closed']
        return p

    def draw_esp_box(self, pos: Tuple[int, int], size: Tuple[int, int],
                    color: Tuple[int, int, int, int], thickness: int = 2):
        """绘制ESP方框（带角标）"""
        scaled_pos = (self.scale_value(pos[0]), self.scale_value(pos[1]))
        scaled_size = (self.scale_value(size[0]), self.scale_value(size[1]))

        x, y, w, h = scaled_pos[0], scaled_pos[1], scaled_size[0], scaled_size[1]
        corner_size = min(self.scale_value(15), w // 4, h // 4)
        scaled_thickness = self.scale_value(thickness)

        # 绘制四个角
        lines = [
            ((x, y), (x + corner_size, y)),  # 左上横
            ((x, y), (x, y + corner_size)),  # 左上竖
            ((x + w, y), (x + w - corner_size, y)),  # 右上横
            ((x + w, y), (x + w, y + corner_size)),  # 右上竖
            ((x, y + h), (x + corner_size, y + h)),  # 左下横
            ((x, y + h), (x, y + h - corner_size)),  # 左下竖
            ((x + w, y + h), (x + w - corner_size, y + h)),  # 右下横
            ((x + w, y + h), (x + w, y + h - corner_size)),  # 右下竖
        ]

        for start, end in lines:
            pygame.draw.line(self.buffer_surface, color, start, end, scaled_thickness)


    def _scale_point(self, p: Tuple[int, int]) -> Tuple[int, int]:
        return (self.scale_value(p[0]), self.scale_value(p[1]))

    def draw_line(self, start: Tuple[int, int], end: Tuple[int, int], color: Tuple[int, int, int, int], width: int = 1):
        s, e = self._scale_point(start), self._scale_point(end)
        pygame.draw.line(self.buffer_surface, color, s, e, self.scale_value(width))

    def draw_rect(self, pos: Tuple[int, int], size: Tuple[int, int], color: Tuple[int, int, int, int], thickness: int = 1, radius: int = 0):
        rect = pygame.Rect(self.scale_value(pos[0]), self.scale_value(pos[1]), self.scale_value(size[0]), self.scale_value(size[1]))
        pygame.draw.rect(self.buffer_surface, color, rect, self.scale_value(thickness), border_radius=self.scale_value(radius))

    def draw_filled_rect(self, pos: Tuple[int, int], size: Tuple[int, int], color: Tuple[int, int, int, int], radius: int = 0):
        rect = pygame.Rect(self.scale_value(pos[0]), self.scale_value(pos[1]), self.scale_value(size[0]), self.scale_value(size[1]))
        pygame.draw.rect(self.buffer_surface, color, rect, border_radius=self.scale_value(radius))

    def draw_circle(self, center: Tuple[int, int], radius: int, color: Tuple[int, int, int, int], thickness: int = 1):
        c = self._scale_point(center)
        r = self.scale_value(radius)
        if thickness <= 0:
            pygame.gfxdraw.filled_circle(self.buffer_surface, c[0], c[1], r, color)
            pygame.gfxdraw.aacircle(self.buffer_surface, c[0], c[1], r, color)
        else:
            pygame.gfxdraw.aacircle(self.buffer_surface, c[0], c[1], r, color)
            if thickness > 1:
                pygame.draw.circle(self.buffer_surface, color, c, r, self.scale_value(thickness))

    def draw_polyline(self, points: List[Tuple[int, int]], color: Tuple[int, int, int, int], width: int = 1):
        if not points or len(points) < 2:
            return
        scaled = [self._scale_point(p) for p in points]
        pygame.draw.lines(self.buffer_surface, color, False, scaled, self.scale_value(width))

    def draw_crosshair(self, center: Tuple[int, int], size: int = 10, gap: int = 4, thickness: int = 1, color: Tuple[int, int, int, int] = (255, 255, 255, 255)):
        c = self._scale_point(center)
        s = self.scale_value(size)
        g = self.scale_value(gap)
        t = self.scale_value(thickness)
        pygame.draw.line(self.buffer_surface, color, (c[0] - g - s, c[1]), (c[0] - g, c[1]), t)
        pygame.draw.line(self.buffer_surface, color, (c[0] + g, c[1]), (c[0] + g + s, c[1]), t)
        pygame.draw.line(self.buffer_surface, color, (c[0], c[1] - g - s), (c[0], c[1] - g), t)
        pygame.draw.line(self.buffer_surface, color, (c[0], c[1] + g), (c[0], c[1] + g + s), t)

    def draw_fov_circle(self, center: Tuple[int, int], radius: int, color: Tuple[int, int, int, int]):
        self.draw_circle(center, radius, color, thickness=1)

    def draw_progress_bar(self, pos: Tuple[int, int], size: Tuple[int, int], value: float, min_val: float, max_val: float, bg_color: Optional[Tuple[int, int, int, int]] = None, fill_color: Optional[Tuple[int, int, int, int]] = None):
        bg = bg_color or self.style['progress']['bg_color']
        fill = fill_color or self.style['progress']['fill_color']
        self.draw_filled_rect(pos, size, bg, radius=3)
        if max_val == min_val:
            pct = 0.0
        else:
            pct = (value - min_val) / (max_val - min_val)
        pct = max(0.0, min(1.0, pct))
        fill_w = int(size[0] * pct)
        self.draw_filled_rect(pos, (fill_w, size[1]), fill, radius=3)

    def draw_content(self):
        """
        用户自定义绘制内容的方法
        子类应该重写此方法来实现具体的绘制逻辑
        """
        # 默认显示FPS
        self.draw_text(self.fps_text, (self.screen_width - 150, 20), (255, 255, 255, 255), size=16)

    def draw_tracer(self, target_pos: Tuple[int, int], color: Tuple[int, int, int, int] = (255, 255, 255, 255), from_bottom: bool = True):
        start = (self.screen_width // 2, self.screen_height - 5) if from_bottom else (self.screen_width // 2, self.screen_height // 2)
        self.draw_line(start, target_pos, color, width=1)

    def render_loop(self):
        """主渲染循环"""
        while self.running:
            try:
                # 清空表面
                self.buffer_surface.fill((0, 0, 0, 0))

                # 更新输入（全局鼠标位置/按键）
                self.update_input()
                # 重置本帧的后绘制覆盖层列表
                self.overlay_draws = []

                # 调用用户自定义的绘制方法
                self.draw_content()

                # 后绘制覆盖层（如下拉列表）按优先级绘制到最上层
                if getattr(self, 'overlay_draws', None):
                    try:
                        for _, fn in sorted(self.overlay_draws, key=lambda x: x[0]):
                            fn()
                    except Exception:
                        pass

                # 清空主屏幕并绘制缓冲
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.buffer_surface, (0, 0))
                pygame.display.flip()

                # 性能监控

                self.clock.tick(self.fps)
                self.frame_count += 1
                current_time = time.time()
                if current_time - self.last_time >= 0.5:
                    actual_fps = self.frame_count / (current_time - self.last_time)
                    self.fps_text = f"FPS: {actual_fps:.1f}"
                    self.frame_count = 0
                    self.last_time = current_time

            except Exception as e:
                print(f"渲染错误: {e}")
                import traceback
                traceback.print_exc()
                break

    def run(self):
        """运行GUI"""
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        self.running = False

                time.sleep(0.01)

        finally:
            self.running = False
            pygame.quit()


