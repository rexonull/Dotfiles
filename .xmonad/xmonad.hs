import XMonad
import Data.Monoid
import System.Exit
import XMonad.Hooks.ManageDocks
import XMonad.Util.Run
import XMonad.Util.SpawnOnce
import Graphics.X11.ExtraTypes.XF86
import XMonad.Layout.Spacing
import XMonad.Layout.NoBorders
import XMonad.Hooks.SetWMName
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.ManageHelpers
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.DynamicBars
import XMonad.Util.EZConfig(additionalKeys, additionalKeysP, additionalMouseBindings)

import qualified XMonad.StackSet as W
import qualified Data.Map        as M

myTerminal      = "termite"

myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True

myClickJustFocuses :: Bool
myClickJustFocuses = True

myBorderWidth   = 0

myModMask       = mod4Mask

myWorkspaces    = [" web "," code "," chat "," game "," mail "," gfx "," 7 "," music "," misc "]

myNormalBorderColor  = "#abb2bf"
myFocusedBorderColor = "#e06c75"

------------------------------------------------------------------------

myKeysAdd :: [(String, X())]
myKeysAdd = [ ("M-r",                       spawn "sxiv /home/rexonull/Pictures/routine.jpg")
            , ("M-S-<Delete>",              spawn "betterlockscreen -s")
            , ("M-C-s",                     spawn "scrot -e 'mv $f ~/Pictures/Screenshots && notify-send screenshot taken'")
            , ("M-S-s",                     spawn "scrot -e 'mv $f ~/Documents/notes && notify-send screenshot taken'")
            , ("M-C-<Return>",              spawn "rofi -show drun -fullscreen")

            -- Volume and Brightness
            , ("<XF86AudioLowerVolume>",    spawn "amixer set Master 5%- unmute")
            , ("<XF86AudioRaiseVolume>",    spawn "amixer set Master 5%+ unmute")
            , ("<XF86MonBrightnessUp>",     spawn "xbacklight -inc 1")
            , ("<XF86MonBrightnessDown>",   spawn "xbacklight -dec 1")

            -- Programs
            , ("M-b",                       spawn "firefox")
            , ("M-C-f",                     spawn "pcmanfm")
            , ("M-m",                       spawn "java -jar /home/rexonull/My/minecraft/TLauncher-2.71.jar")

            , ("M-f",                       spawn (myTerminal ++ " -e ranger"))
            , ("M-v",                       spawn (myTerminal ++ " -e vim"))
            , ("M-M1-x",                    spawn (myTerminal ++ " -e 'vim /home/rexonull/.xmonad/xmonad.hs'"))
            , ("M-M1-b",                    spawn (myTerminal ++ " -e 'vim /home/rexonull/.config/xmobar/xmobarrc'"))
            , ("M-<F1>",                    spawn "setxkbmap us")
            , ("M-<F2>",                    spawn "setxkbmap np")
            ]


myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

    [ ((modm,               xK_Return), spawn $ XMonad.terminal conf)
    , ((modm,               xK_space ), spawn "dmenu_run -nb '#161821' -nf '#c6c8d1' -sb '#b4be82' -sf '#002329' -h 25")
    -- close focused window
    , ((modm .|. shiftMask, xK_c     ), kill)
     -- Rotate through the available layout algorithms
    , ((modm,               xK_Tab   ), sendMessage NextLayout)
    --  Reset the layouts on the current workspace to default
    , ((modm .|. shiftMask, xK_Tab   ), setLayout $ XMonad.layoutHook conf)
    -- Resize viewed windows to the correct size
    , ((modm,               xK_n     ), refresh)
    -- Move focus to the next window
    , ((modm,               xK_j     ), windows W.focusDown)
    -- Move focus to the previous window
    , ((modm,               xK_k     ), windows W.focusUp  )
    -- Move focus to the master window
    , ((modm,               xK_m     ), windows W.focusMaster  )
    -- Swap the focused window and the master window
    , ((modm .|. shiftMask, xK_Return), windows W.swapMaster)
    -- Swap the focused window with the next window
    , ((modm .|. shiftMask, xK_j     ), windows W.swapDown  )
    -- Swap the focused window with the previous window
    , ((modm .|. shiftMask, xK_k     ), windows W.swapUp    )
    -- Shrink the master area
    , ((modm,               xK_h     ), sendMessage Shrink)
    -- Expand the master area
    , ((modm,               xK_l     ), sendMessage Expand)
    -- Push window back into tiling
    , ((modm,               xK_t     ), withFocused $ windows . W.sink)
    -- Increment the number of windows in the master area
    , ((modm              , xK_comma ), sendMessage (IncMasterN 1))
    -- Deincrement the number of windows in the master area
    , ((modm              , xK_period), sendMessage (IncMasterN (-1)))
    -- Use this binding with avoidStruts from Hooks.ManageDocks.
    , ((modm .|. shiftMask, xK_f     ), sendMessage ToggleStruts)

    -- Quit xmonad
    , ((modm .|. shiftMask .|. mod1Mask, xK_q     ), io (exitWith ExitSuccess))
    -- Restart xmonad
    , ((modm              , xK_q     ), spawn "xmonad --recompile; xmonad --restart")
    ]
    ++
    --
    -- mod-[1..9], Switch to workspace N
    -- mod-shift-[1..9], Move client to workspace N
    --
    [((m .|. modm, k), windows $ f i)
        | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
        , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)]]
    ++
    --
    -- mod-{w,e,r}, Switch to physical/Xinerama screens 1, 2, or 3
    -- mod-shift-{w,e,r}, Move client to screen 1, 2, or 3
    --
    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
        | (key, sc) <- zip [xK_w, xK_e, xK_r] [0..]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]



------------------------------------------------------------------------
-- Mouse bindings: default actions bound to mouse events
--
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $

    -- mod-button1, Set the window to floating mode and move by dragging
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))
    -- mod-button2, Raise the window to the top of the stack
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))
    -- mod-button3, Set the window to floating mode and resize by dragging
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))
    -- you may also bind events to the mouse scroll wheel (button4 and button5)
    ]

------------------------------------------------------------------------
-- Layouts:

-- You can specify and transform your layouts by modifying these values.
-- If you change layout bindings be sure to use 'mod-shift-space' after
-- restarting (with 'mod-q') to reset your layout state to the new
-- defaults, as xmonad preserves your old layout settings by default.
--
-- The available layouts.  Note that each layout is separated by |||,
-- which denotes layout choice.
--
myLayout = smartBorders . avoidStruts $ noBorders (Full) ||| tiled ||| Mirror tiled
  where
     -- default tiling algorithm partitions the screen into two panes
     tiled   = spacing 5 $ Tall nmaster delta ratio

     -- The default number of windows in the master pane
     nmaster = 1

     -- Default proportion of screen occupied by master pane
     ratio   = 1/2

     -- Percent of screen to increment by when resizing panes
     delta   = 3/100

------------------------------------------------------------------------
-- Window rules:

-- Execute arbitrary actions and WindowSet manipulations when managing
-- a new window. You can use this to, for example, always float a
-- particular program, or have a client always appear on a particular
-- workspace.
--
-- To find the property name associated with a program, use
-- > xprop | grep WM_CLASS
-- and click on the client you're interested in.
--
-- To match on the WM_NAME, you can use 'title' in the same way that
-- 'className' and 'resource' are used below.
--
myManageHook = composeAll
    [ manageDocks
    , isFullscreen                  --> doFullFloat
    , className =? "MPlayer"        --> doFloat
    , className =? "Gimp"           --> doFloat
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore
    , manageHook defaultConfig
    ]

------------------------------------------------------------------------
-- Event handling

-- * EwmhDesktops users should change this to ewmhDesktopsEventHook
--
-- Defines a custom handler function for X Events. The function should
-- return (All True) if the default handler is to be run afterwards. To
-- combine event hooks use mappend or mconcat from Data.Monoid.
--
myEventHook = mempty

------------------------------------------------------------------------
-- Startup hook

-- Perform an arbitrary action each time xmonad starts or is restarted
-- with mod-q.  Used by, e.g., XMonad.Layout.PerWorkspace to initialize
-- per-workspace layout choices.
myStartupHook = do
    spawnOnce "nitrogen --restore &"
    spawnOnce "picom &"
    spawnOnce "lxappearance &"
    spawnOnce "nm-applet &"
    spawnOnce "exec /usr/bin/trayer --edge top --align center --SetDockType true --SetPartialStrut true --expand true --width 6 --transparent true --alpha 0 --height 25 --tint 0x2b2d3a"
    setWMName "LG3D"

main = do
    xmproc <- spawnPipe "xmobar -x 0 $HOME/.config/xmobar/xmobarrc0"
    xmproc <- spawnPipe "xmobar -x 1 $HOME/.config/xmobar/xmobarrc1"
    xmonad $ docks $ def {
      -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = myLayout,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        logHook            = dynamicLogWithPP $ def { ppOutput = hPutStrLn xmproc
                                                    , ppCurrent = xmobarColor "#bb97ee" "" . wrap "-" "-"
                                                    , ppVisible = xmobarColor "#6dcae8" ""
                                                    , ppHidden = xmobarColor "#6dcae8" ""
                                                    , ppHiddenNoWindows = xmobarColor "#34535e" ""
                                                    , ppTitle = xmobarColor "#6dcae8" "" . shorten 50
                                                    , ppSep = "  |  "
                                                    , ppLayout = xmobarColor "#6dcae8" ""
                                                    , ppUrgent = xmobarColor "#e27878" "" . wrap "!" "!"
                                                    },

        startupHook        = myStartupHook
    } `additionalKeysP` myKeysAdd
