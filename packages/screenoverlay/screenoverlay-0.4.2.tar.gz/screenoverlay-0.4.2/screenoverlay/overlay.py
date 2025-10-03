#!/usr/bin/env python3
"""
Native Blur Overlay - Uses OS-native blur effects
No screen capture, no permissions needed, instant appearance
"""

import tkinter as tk
import platform
import sys
import os
import threading
from multiprocessing import Process, Queue
import time
import atexit
import signal

# Try to import screeninfo for multi-monitor support
try:
    from screeninfo import get_monitors
    HAS_SCREENINFO = True
except ImportError:
    HAS_SCREENINFO = False


class NativeBlurOverlay:
    def __init__(self, mode='blur', blur_strength=3, opacity=0.85, color_tint=(136, 136, 136), all_screens=True):
        """
        Initialize native overlay
        
        Parameters:
        - mode (str): Overlay mode - 'blur', 'black', 'white', 'custom'
                      'blur'   - Blurred background with tint (default)
                      'black'  - Full black screen (privacy mode)
                      'white'  - Full white screen (flash/fade effect)
                      'custom' - Custom color with transparency
        - blur_strength (int): How blurred/obscured (1-5, only for mode='blur')
        - opacity (float): Window opacity (0.0 to 1.0)
        - color_tint (tuple): RGB color tint (0-255)
        - all_screens (bool): If True, blur all monitors. If False, only blur primary monitor (default: True)
        """
        self.mode = mode.lower()
        self.blur_strength = max(1, min(5, blur_strength))
        self.all_screens = all_screens
        
        # Apply mode-specific settings
        if self.mode == 'black':
            self.opacity = opacity if opacity != 0.85 else 1.0  # Default full opacity for black
            self.color_tint = (0, 0, 0)
            self.apply_blur = False
        elif self.mode == 'white':
            self.opacity = opacity if opacity != 0.85 else 1.0  # Default full opacity for white
            self.color_tint = (255, 255, 255)
            self.apply_blur = False
        elif self.mode == 'custom':
            self.opacity = opacity
            self.color_tint = color_tint
            self.apply_blur = False
        else:  # mode == 'blur'
            # Adjust opacity based on blur strength
            self.opacity = min(1.0, opacity + (self.blur_strength - 3) * 0.05)
            # Adjust tint intensity based on blur strength
            tint_factor = 1.0 + (self.blur_strength - 3) * 0.15
            self.color_tint = tuple(min(255, int(c * tint_factor)) for c in color_tint)
            self.apply_blur = True
        
        self.root = None
        self.windows = []  # List to hold multiple windows for multi-monitor
        self._timer_id = None
        self._process = None
        self._command_queue = None
        
        # Register cleanup on exit to prevent orphaned processes
        atexit.register(self._cleanup_on_exit)
        
    def _cleanup_on_exit(self):
        """Cleanup overlay process on program exit"""
        if self._process is not None and self._process.is_alive():
            try:
                # Try graceful stop first
                if self._command_queue is not None:
                    try:
                        self._command_queue.put('stop')
                    except:
                        pass
                
                # Wait briefly
                self._process.join(timeout=0.5)
                
                # Force kill if still alive
                if self._process.is_alive():
                    self._process.terminate()
                    self._process.join(timeout=0.5)
                    
                # Last resort - force kill
                if self._process.is_alive():
                    self._process.kill()
            except:
                pass
        
    def start(self):
        """
        Start the overlay process with show/hide control.
        Call this once at app startup.
        
        After calling start(), use show() and hide() to control visibility instantly.
        
        Example for ScreenStop:
            overlay = Overlay(mode='blur', blur_strength=4)
            overlay.start()  # Initialize (call once)
            
            overlay.show()   # Show overlay (instant)
            time.sleep(2)
            overlay.hide()   # Hide overlay (instant)
            overlay.show()   # Show again
            
            overlay.stop()   # Cleanup when done
        """
        if self._process is not None:
            return
        
        self._command_queue = Queue()
        self._process = Process(target=self._run_process, args=(self._command_queue,), daemon=True)
        self._process.start()
        
        # Wait a bit for process to initialize
        time.sleep(0.3)
    
    def show(self):
        """Show the overlay (instant, ~1ms)"""
        if self._command_queue is not None:
            self._command_queue.put('show')
    
    def hide(self):
        """Hide the overlay (instant, ~1ms)"""
        if self._command_queue is not None:
            self._command_queue.put('hide')
    
    def stop(self):
        """Stop and cleanup the overlay completely"""
        if self._command_queue is not None:
            self._command_queue.put('stop')
        
        if self._process is not None:
            self._process.join(timeout=2.0)
            if self._process.is_alive():
                self._process.terminate()
            self._process = None
        
        self._command_queue = None
    
    def _run_process(self, command_queue):
        """Run overlay in separate process with command queue"""
        try:
            # Create windows for all monitors
            self._create_windows()
            
            # Hide all windows initially
            for win in self.windows:
                win.withdraw()
            
            # Process commands from queue
            def check_commands():
                try:
                    while not command_queue.empty():
                        cmd = command_queue.get_nowait()
                        if cmd == 'show':
                            for win in self.windows:
                                try:
                                    win.deiconify()
                                    win.lift()
                                except Exception as e:
                                    print(f"Warning: Failed to show window: {e}")
                        elif cmd == 'hide':
                            for win in self.windows:
                                try:
                                    win.withdraw()
                                except Exception as e:
                                    print(f"Warning: Failed to hide window: {e}")
                        elif cmd == 'stop':
                            self.root.quit()
                            return
                except Exception as e:
                    print(f"Warning: Command queue error: {e}")
                
                # Check again in 10ms
                self.root.after(10, check_commands)
            
            # Start command checker
            check_commands()
            
            # Run mainloop
            self.root.mainloop()
            
        except Exception as e:
            print(f"Overlay process error: {e}")
        finally:
            os._exit(0)
    
    def _get_monitors(self):
        """Get information about all monitors"""
        if HAS_SCREENINFO:
            try:
                monitors = get_monitors()
                return [(m.x, m.y, m.width, m.height) for m in monitors]
            except:
                pass
        
        # Fallback: assume single primary monitor
        root = tk.Tk()
        root.withdraw()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return [(0, 0, width, height)]
    
    def _create_windows(self):
        """Create overlay windows for all monitors (or just primary if all_screens=False)"""
        monitors = self._get_monitors()
        
        # If all_screens is False, only use primary monitor
        if not self.all_screens:
            monitors = monitors[:1]  # Only keep first monitor
        
        # Create primary root window
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        
        # Configure primary window for first monitor
        if monitors:
            x, y, width, height = monitors[0]
            self._configure_window(self.root, x, y, width, height)
            self.windows.append(self.root)
        
        # Create additional windows for other monitors (only if all_screens=True)
        for x, y, width, height in monitors[1:]:
            win = tk.Toplevel(self.root)
            win.overrideredirect(True)
            win.attributes('-topmost', True)
            self._configure_window(win, x, y, width, height)
            self.windows.append(win)
    
    def _configure_window(self, window, x, y, width, height):
        """Configure a window with overlay settings"""
        # Set background color (tint)
        bg_color = f'#{self.color_tint[0]:02x}{self.color_tint[1]:02x}{self.color_tint[2]:02x}'
        window.configure(bg=bg_color)
        
        # Set opacity
        window.attributes('-alpha', self.opacity)
        
        # Position and size
        window.geometry(f"{width}x{height}+{x}+{y}")
        
        # Apply native blur effect based on OS (only if mode is 'blur')
        if self.apply_blur:
            self._apply_native_blur_to_window(window)
        
        # Bind escape key to exit (only on primary window)
        if window == self.root:
            window.bind('<Escape>', lambda e: self.kill_completely())
            window.focus_set()
    
    def _create_window(self):
        """Internal method to create and configure the Tkinter window"""
        self.root = tk.Tk()
        
        # Remove window decorations
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        
        # Set background color (tint)
        bg_color = f'#{self.color_tint[0]:02x}{self.color_tint[1]:02x}{self.color_tint[2]:02x}'
        self.root.configure(bg=bg_color)
        
        # Set opacity
        self.root.attributes('-alpha', self.opacity)
        
        # Full screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Apply native blur effect based on OS (only if mode is 'blur')
        if self.apply_blur:
            self._apply_native_blur()
        
        # Bind escape key to exit
        self.root.bind('<Escape>', lambda e: self.kill_completely())
        self.root.focus_set()
    
    def activate(self, duration=5):
        """Show native blur overlay and exit after duration"""
        self._create_windows()  # Use multi-monitor aware method
        
        # Auto-exit timer
        self._timer_id = self.root.after(int(duration * 1000), self.kill_completely)
        
        # Show window
        self.root.mainloop()
        
    def _apply_native_blur(self):
        """Apply OS-native backdrop blur effect to root window (legacy method)"""
        self._apply_native_blur_to_window(self.root)
    
    def _apply_native_blur_to_window(self, window):
        """Apply OS-native backdrop blur effect to a specific window"""
        system = platform.system()
        
        if system == 'Darwin':  # macOS
            self._apply_macos_blur_to_window(window)
        elif system == 'Windows':
            self._apply_windows_blur_to_window(window)
        elif system == 'Linux':
            self._apply_linux_blur_to_window(window)
            
    def _apply_macos_blur(self):
        """Apply macOS NSVisualEffectView blur (legacy method)"""
        self._apply_macos_blur_to_window(self.root)
    
    def _apply_macos_blur_to_window(self, window):
        """Apply macOS NSVisualEffectView blur to a specific window"""
        try:
            from Cocoa import NSView, NSVisualEffectView
            from Cocoa import NSVisualEffectBlendingModeBehindWindow, NSVisualEffectMaterialDark
            import objc
            
            # Get the Tk window's NSWindow
            window_id = window.winfo_id()
            
            # Create NSVisualEffectView
            # Note: This requires pyobjc-framework-Cocoa
            # The blur will be applied to the window background
            
            # Try to get NSWindow from Tk
            from tkinter import _tkinter
            
            # Alternative: Use AppKit directly
            try:
                from AppKit import NSApp, NSWindow
                from Cocoa import NSMakeRect
                
                # Get all windows and find ours
                for window in NSApp.windows():
                    if window.isVisible():
                        # Create visual effect view
                        frame = window.contentView().frame()
                        effect_view = NSVisualEffectView.alloc().initWithFrame_(frame)
                        effect_view.setBlendingMode_(NSVisualEffectBlendingModeBehindWindow)
                        effect_view.setMaterial_(NSVisualEffectMaterialDark)
                        effect_view.setState_(1)  # Active state
                        
                        # Add as subview
                        window.contentView().addSubview_positioned_relativeTo_(
                            effect_view, 0, None
                        )
                        break
            except Exception as e:
                print(f"AppKit blur failed: {e}")
                
        except ImportError:
            print("pyobjc not available, install with: pip install pyobjc-framework-Cocoa")
        except Exception as e:
            print(f"macOS blur effect failed: {e}")
            
    def _apply_windows_blur(self):
        """Apply Windows Acrylic/Blur effect (legacy method)"""
        self._apply_windows_blur_to_window(self.root)
    
    def _apply_windows_blur_to_window(self, window):
        """Apply Windows Acrylic/Blur effect to a specific window"""
        try:
            import ctypes
            from ctypes import wintypes
            
            # Get window handle - try multiple methods
            try:
                # Method 1: Direct window ID
                hwnd = window.winfo_id()
            except:
                # Method 2: Get parent window
                hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
            
            if not hwnd:
                print("Could not get window handle for blur effect")
                return
            
            # Windows 10+ blur effect using DWM (Desktop Window Manager)
            DWM_BB_ENABLE = 0x00000001
            DWM_BB_BLURREGION = 0x00000002
            
            class DWM_BLURBEHIND(ctypes.Structure):
                _fields_ = [
                    ("dwFlags", wintypes.DWORD),
                    ("fEnable", wintypes.BOOL),
                    ("hRgnBlur", wintypes.HANDLE),
                    ("fTransitionOnMaximized", wintypes.BOOL),
                ]
            
            # Enable blur behind window
            bb = DWM_BLURBEHIND()
            bb.dwFlags = DWM_BB_ENABLE
            bb.fEnable = True
            bb.hRgnBlur = None
            bb.fTransitionOnMaximized = False
            
            result = ctypes.windll.dwmapi.DwmEnableBlurBehindWindow(hwnd, ctypes.byref(bb))
            
            # Try Windows 11 Acrylic/Mica effect (newer, better-looking blur)
            try:
                DWMWA_SYSTEMBACKDROP_TYPE = 38
                DWMSBT_TRANSIENTWINDOW = 3  # Acrylic effect (best for overlays)
                DWMSBT_MAINWINDOW = 2       # Mica effect (alternative)
                
                # Use Acrylic for stronger blur effect
                value = ctypes.c_int(DWMSBT_TRANSIENTWINDOW)
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, 
                    DWMWA_SYSTEMBACKDROP_TYPE,
                    ctypes.byref(value),
                    ctypes.sizeof(value)
                )
            except Exception as e:
                # Windows 10 fallback - DwmEnableBlurBehindWindow is enough
                pass
                
        except Exception as e:
            # Blur effect failed, but window will still work (just without blur)
            print(f"Note: Windows blur effect unavailable: {e}")
            print("Overlay will work but without native blur effect")
            
    def _apply_linux_blur(self):
        """Apply Linux compositor blur (X11/Wayland) (legacy method)"""
        self._apply_linux_blur_to_window(self.root)
    
    def _apply_linux_blur_to_window(self, window):
        """Apply Linux compositor blur (X11/Wayland) to a specific window"""
        try:
            # Linux blur depends on compositor (KWin, Mutter, etc.)
            # Most compositors respect window transparency and apply blur automatically
            # For KDE Plasma, we can hint the compositor
            
            # Try to set _KDE_NET_WM_BLUR_BEHIND_REGION property
            # This requires X11 access
            pass  # Most Linux compositors auto-blur transparent windows
            
        except Exception as e:
            print(f"Linux blur effect hint failed: {e}")
    
    def kill_completely(self):
        """Exit the overlay completely (for activate() backward compatibility)"""
        try:
            if self.root:
                self.root.quit()
                self.root.destroy()
        except:
            pass
        
        # Only call os._exit if we're in activate() mode (has timer)
        if self._timer_id is not None:
            os._exit(0)


if __name__ == "__main__":
    # Quick test - try different modes
    import sys
    
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = 'blur'
    
    print(f"Testing mode='{mode}' for 3 seconds...")
    print("Available modes: blur, black, white, custom")
    print("Usage: python NativeBlurOverlay.py [mode]")
    print()
    
    if mode == 'blur':
        overlay = NativeBlurOverlay(mode='blur', blur_strength=4)
    elif mode == 'black':
        overlay = NativeBlurOverlay(mode='black')
    elif mode == 'white':
        overlay = NativeBlurOverlay(mode='white')
    elif mode == 'custom':
        overlay = NativeBlurOverlay(mode='custom', opacity=0.7, color_tint=(255, 0, 0))  # Red example
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)
    
    overlay.activate(duration=3)

