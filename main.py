def on_button_a():
    basic.show_icon(IconNames.COW)
    basic.set_led_colors(0xff0000, 0xffffff, 0xffffff, 100)
    music.play(music.string_playable("C E D F E G F A ", 120),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_event(Button.A,
    input.button_event_value(ButtonEvent.LONG_CLICK),
    on_button_a)

def on_button_ab():
    basic.show_icon(IconNames.GIRAFFE)
    basic.set_led_colors(0xffffff, 0xffff00, 0xffffff)
    music.play(music.string_playable("C E D F E G F A ", 120),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_event(Button.AB,
    input.button_event_value(ButtonEvent.LONG_CLICK),
    on_button_ab)

def on_button_b():
    basic.show_icon(IconNames.TORTOISE)
    basic.set_led_colors(0xffffff, 0xffffff, 0x00ff00)
    music.play(music.string_playable("C E D F E G F A ", 120),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_event(Button.B,
    input.button_event_value(ButtonEvent.LONG_CLICK),
    on_button_b)

def on_gesture_screen_down():
    basic.show_leds("""
        . # # # .
        # # . # #
        # . . . #
        # . # . #
        . # # # .
        """)
    control.wait_micros(5000000)
    basic.show_leds("""
        # # # # .
        . . . . #
        . # . . #
        # # # # .
        . # . . .
        """)
    control.wait_micros(5000000)
    basic.show_string("Neu Start,  Schüüüs ")
    control.wait_micros(5000000)
    control.reset()
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_a2():
    control.wait_micros(150000)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        # # # # #
        . # # # .
        """)
    control.wait_micros(150000)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # . .
        # # # . .
        . # # # .
        """)
    control.wait_micros(150000)
    basic.show_leds("""
        . . # . .
        . # # . .
        # # . . .
        # # . . .
        . # # . .
        """)
    control.wait_micros(150000)
    basic.show_leds("""
        . . . . .
        . # . . .
        # # . . .
        # # . . .
        . # . . .
        """)
    control.wait_micros(150000)
    basic.show_leds("""
        . . . . .
        . # . . .
        # . . . .
        # . . . .
        . # . . .
        """)
    control.wait_micros(150000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_event(Button.A, input.button_event_click(), on_button_a2)

def on_gesture_shake():
    basic.show_leds("""
        . . # . .
        . # # # .
        # # . # #
        . # # # .
        . . # . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_b2():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    control.wait_micros(15000)
    basic.show_leds("""
        . # # . .
        . # # . .
        . . . . .
        . . . . .
        . . . . .
        """)
    control.wait_micros(15000)
    basic.show_leds("""
        . . . . .
        . # # . .
        . # # . .
        . . . . .
        . . . . .
        """)
    control.wait_micros(15000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # . .
        . # # . .
        . . . . .
        """)
    control.wait_micros(15000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # # . .
        . # # . .
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . # # . .
        . # # . .
        . . . . .
        . . . . .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . # # . .
        . # # . .
        . . . . .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # . .
        . # # . .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # # . .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # # # .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . # # . .
        . # # . .
        . . . . .
        . # # # .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . # # . .
        . # # . .
        . # # # .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # . .
        . # # # .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # # # # #
        """)
    control.wait_micros(10000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # # # # #
        """)
input.on_button_event(Button.B,
    input.button_event_value(ButtonEvent.CLICK),
    on_button_b2)

basic.show_icon(IconNames.GIRAFFE)
basic.set_led_colors(0xffffff, 0xffff00, 0xffffff)
music.play(music.create_sound_expression(WaveShape.NOISE,
        1,
        5000,
        255,
        255,
        1000,
        SoundExpressionEffect.WARBLE,
        InterpolationCurve.LOGARITHMIC),
    music.PlaybackMode.IN_BACKGROUND)