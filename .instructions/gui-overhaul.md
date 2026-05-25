The program has been functional and running for a few days. I have received feedback and would like to start on a few changes. The main task is modifying the geometry of the layout itself. I have added a new folder (layout-example) that contains 'keyboard-layout.htm'. This htm file contains a keyboard layout that I generated in CSS to show the exact layout I would like to copy. This new layout is based on a standard ANSI TKL keyboard with additional buttons located within that framework for our custom controls. A few specific notes about the new layout:

#### Modified ANSI TKL CSS Layout
- The layout utilizes a fractional grid system derived from the Mechanical Engineering standard for keycaps:
- Grid Granularity: A 60-column grid represents the 15U width of the main cluster (60×0.25U). This allows for the precise placement of non-integer unit keys like the 1.25U modifiers and 6.25U spacebar.
- Structural Modularity: The DOM is structured into two primary clusters (main, edit) to maintain visual separation while enforcing the horizontal alignment required ANSI TKL keyboard.
- Proportional Accuracy:
  - Tab/Backslash: 1.5U (6×0.25U).
  - Caps Lock: 1.75U (7×0.25U).
  - Enter/LShift: 2.25U (9×0.25U).
  - RShift: 2.75U (11×0.25U).
  - Spacebar: 6.25U (25×0.25U).
- Styling: Utilizes CSS variables for the base unit (--u), facilitating global scaling of the keyboard without breaking the relative proportions of the keycaps.

#### General
- The layout is broken into two clusters:
  - main-cluster: this is the left section of the keyboard, housing the typical 15U row and all columns.  
  - edit-cluster: this houses the typical keys to the right of the main-cluster such as Insert, Home, End, Del... and also arrow keys.
- Note: there is no numpad cluster which would naturally be the next listed. The numpad is intentionally left off in favor of a TKL style base layout.
  
#### Additional Keys/Changes
- New top row for both main-cluster and edit-cluster.
- main-cluster:
  - Esc has been added to the top left of the main-cluster.
  - Function keys F1 through F12 have been added to the top row.
  - Super and Menu have been added between on the bottom row between right alt and right ctrl. 
  - EXIT has moved to the typically empty location between ESC and F1.
- edit-cluster:
  - The directional GUI control keys have been moved to the top row, aligned horizontally with the main-cluster's Function keys. These are still half height full width. They are located where the usual PrtSc, Scroll, Pause buttons would be, but I am not including those three buttons as they do not get much use and the space works well for the directional controls.
  - Insert, Home, PgUp, Del, End, PgDn have been added.
  - VOL-, MUTE, VOL+ have been added in the typically empty location below the Del, End, PgDn, keys.
  - Directional arrows have been added.
  - The zoom-in and zoom-out control buttons have been migrated to the left and right of the up arrow.

#### Other notes:
- I would like to mimic the layout of the .htm as much as possible. There are some hard-coded px sizes, so up to the best way to navigate maintaining the functionality of the zoom-in and zoom-out features. Otherwise I tried to size everything based off a fundamental "U" scale, which should adjust everything proportionally. However, I am aiming to mimic the layout, the actual CSS used or specifics defined in the CSS are absolutely not law. When presented with two potential solutions to a problem, always choose the one that helps the overall project more in lieu of adherence to the CSS.
- I would also like to keep any of the formatting/styling where possible, including coloring. At the same time, I would very much like to keep the current interactive key-highlighting.
- The aspect ratio of the full keyboard will be wider with this new layout. I would like to keep the full size approximately the same heigh as the existing keyboard, if it needs to go wider that is fine as long as it doesn't extend past the monitor.
- I am abandoning the svg files in favor of text based indicators. When I tried to package the app it added a layer of complication and some end users had issues with them rendering. I have moved the .svg files to a ./old-assets folder to keep them for low-potential future use.

