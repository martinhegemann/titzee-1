input.onButtonEvent(Button.A, input.buttonEventValue(ButtonEvent.LongClick), function () {
    basic.showIcon(IconNames.Cow)
    basic.setLedColors(0xff0000, 0xffffff, 0xffffff, 100)
    music.play(music.stringPlayable("C E D F E G F A ", 120), music.PlaybackMode.InBackground)
})
input.onButtonEvent(Button.AB, input.buttonEventValue(ButtonEvent.LongClick), function () {
    basic.showIcon(IconNames.Giraffe)
    basic.setLedColors(0xffffff, 0xffff00, 0xffffff)
    music.play(music.stringPlayable("C E D F E G F A ", 120), music.PlaybackMode.InBackground)
})
input.onButtonEvent(Button.B, input.buttonEventValue(ButtonEvent.LongClick), function () {
    basic.showIcon(IconNames.Tortoise)
    basic.setLedColors(0xffffff, 0xffffff, 0x00ff00)
    music.play(music.stringPlayable("C E D F E G F A ", 120), music.PlaybackMode.InBackground)
})
input.onGesture(Gesture.ScreenDown, function () {
    basic.showLeds(`
        . # # # .
        # # . # #
        # . . . #
        # . # . #
        . # # # .
        `)
    control.waitMicros(500000)
    basic.showLeds(`
        # # # # .
        . . . . #
        . # . . #
        # # # # .
        . # . . .
        `)
    control.waitMicros(500000)
    basic.showString("Neu Start,  Schüüüs ")
    control.waitMicros(500000)
    control.reset()
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    control.waitMicros(150000)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        # # # # #
        . # # # .
        `)
    control.waitMicros(150000)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # . .
        # # # . .
        . # # # .
        `)
    control.waitMicros(150000)
    basic.showLeds(`
        . . # . .
        . # # . .
        # # . . .
        # # . . .
        . # # . .
        `)
    control.waitMicros(150000)
    basic.showLeds(`
        . . . . .
        . # . . .
        # # . . .
        # # . . .
        . # . . .
        `)
    control.waitMicros(150000)
    basic.showLeds(`
        . . . . .
        . # . . .
        # . . . .
        # . . . .
        . # . . .
        `)
    control.waitMicros(150000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        . . # . .
        . # # # .
        # # . # #
        . # # # .
        . . # . .
        `)
})
input.onButtonEvent(Button.B, input.buttonEventValue(ButtonEvent.Click), function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    control.waitMicros(15000)
    basic.showLeds(`
        . # # . .
        . # # . .
        . . . . .
        . . . . .
        . . . . .
        `)
    control.waitMicros(15000)
    basic.showLeds(`
        . . . . .
        . # # . .
        . # # . .
        . . . . .
        . . . . .
        `)
    control.waitMicros(15000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # . .
        . # # . .
        . . . . .
        `)
    control.waitMicros(15000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . # # . .
        . # # . .
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . # # . .
        . # # . .
        . . . . .
        . . . . .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . # # . .
        . # # . .
        . . . . .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # . .
        . # # . .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . # # . .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . # # # .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . # # . .
        . # # . .
        . . . . .
        . # # # .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . # # . .
        . # # . .
        . # # # .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # . .
        . # # # .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # # # # #
        `)
    control.waitMicros(10000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # # # # #
        `)
})
basic.showIcon(IconNames.Giraffe)
basic.setLedColors(0xffffff, 0xffff00, 0xffffff)
music.play(music.createSoundExpression(WaveShape.Noise, 1, 5000, 255, 255, 1000, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
