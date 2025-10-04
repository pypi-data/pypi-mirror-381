Epoch Click Behavior: What Changes And Where

  - Purpose: In epochs mode, a left‑click on a trace toggles an epoch’s “bad” state and refreshes the plot to reflect
  per‑epoch colors and bad markers.

  Click Flow

  - Entry: A left‑click on a trace is handled here:
      - src/mne_qt_browser/_graphic_items.py:677
  - Action: The click calls toggle_bad(x) with the x‑position (time):
      - src/mne_qt_browser/_graphic_items.py:689
  - Delegation: In epochs mode, it delegates to MNE‑Python to compute which epoch was clicked and whether to mark/unmark
  it as bad:
      - src/mne_qt_browser/_graphic_items.py:603

  What Actually Changes

  - Epoch color map is updated in memory
      - The “color reference” for the clicked epoch across all channels is rewritten:
          - src/mne_qt_browser/_graphic_items.py:623
      - Initial construction of the epoch color matrix:
          - src/mne_qt_browser/_pg_figure.py:335
      - Pre‑marked bad epochs and bad channels are also encoded at init:
          - src/mne_qt_browser/_pg_figure.py:350
          - src/mne_qt_browser/_pg_figure.py:357
  - Traces are repainted using updated colors
      - Every trace recomputes its color(s) and data after a toggle:
          - src/mne_qt_browser/_graphic_items.py:629
          - src/mne_qt_browser/_graphic_items.py:632
      - Color resolution per trace (including multicolor splitting into child traces):
          - src/mne_qt_browser/_graphic_items.py:471
          - src/mne_qt_browser/_graphic_items.py:507
      - Display segmentation: non‑matching colored segments are hidden (set to NaN) so the currently assigned color is
  visible:
          - src/mne_qt_browser/_graphic_items.py:579
          - src/mne_qt_browser/_graphic_items.py:585
  - Overview bar updates
      - The “bad epoch” shading rectangles are added/removed for the overview bar:
          - src/mne_qt_browser/_graphic_items.py:626
          - src/mne_qt_browser/_widgets.py:814
          - src/mne_qt_browser/_widgets.py:821
          - src/mne_qt_browser/_widgets.py:832

  Theming And Colors

  - All pens/brushes use _get_color(..., invert=self.mne.dark); self.mne.dark is computed from the window palette at
  init:
      - src/mne_qt_browser/_pg_figure.py:258
  - Epoch “bad” overlay in overview bar uses self.mne.epoch_color_bad:
      - src/mne_qt_browser/_widgets.py:827
  - Trace colors are drawn via _get_color(...) with dark/light inversion rules:
      - src/mne_qt_browser/_graphic_items.py:507
      - Color inversion and mapping internals:
          - src/mne_qt_browser/_colors.py:111

  What you can change (common customizations)

  - Click behavior
      - Disable marking on click (browse‑only): short‑circuit in DataTrace.mouseClickEvent(...) so it ignores clicks in
  epochs mode.
          - src/mne_qt_browser/_graphic_items.py:677
  - Colors
      - Change the color used to mark bad epochs globally by adjusting self.mne.epoch_color_bad before plotting.
      - Customize the per‑epoch color scheme by pre‑setting self.mne.epoch_colors (if you want different per‑epoch
  palettes) or by modifying how epoch_color_ref is built:
          - src/mne_qt_browser/_pg_figure.py:335
  - Overview bar overlay
      - Adjust opacity or color of the “bad epoch” rectangles by modifying how the rect pen/brush is created:
          - src/mne_qt_browser/_widgets.py:827
  - Multicolor trace rendering
      - If you want to show all segments together (instead of hiding non‑matching ones), change the NaN masking in
  update_data():
          - src/mne_qt_browser/_graphic_items.py:579
          - src/mne_qt_browser/_graphic_items.py:585
  - Theme stability
      - Avoid dynamic inversion by forcing a fixed theme and using non‑inverted colors (set self.mne.dark consistently or
  bypass inversion in _get_color calls you customize).

  Extension points (where to hook your logic)

  - After toggle, but before repaint
      - Right after _toggle_bad_epoch(...) returns and before epoch_color_ref is updated:
          - src/mne_qt_browser/_graphic_items.py:603
  - While computing trace colors
      - In DataTrace.update_color() if you want to override color selection logic:
          - src/mne_qt_browser/_graphic_items.py:459
  - Overview bar rendering
      - In OverviewBar.update_bad_epochs() for visibility, z‑order, opacity tweaks:
          - src/mne_qt_browser/_widgets.py:814

  Quick mental model

  - Click → find epoch → set that epoch’s target color in epoch_color_ref → repaint traces (color + data masking) →
  refresh overview bar bad rectangles.
  - Everything you see is derived from epoch_color_ref and the “bad epochs/channels” sets; visuals are created with
  _get_color(..., self.mne.dark).

  If you want, I can prototype:

  - A browse‑only flag that disables marking on click.
  - A fixed theme mode to keep colors consistent when embedded.
  - A custom bad‑epoch overlay style (opacity/gradient) and a different trace colormap.


Why did a red color appear when clicking an epoch?

- Short answer: clicking an epoch toggles its state via MNE‑Python and the browser repaints that epoch’s time‑series using a “bad‑epoch” color — by default, red — by overwriting the epoch’s entry in the in‑memory color map. That’s why you saw the time‑series turn red on click.

- Code path that injects the red:
  - Click handler: src/mne_qt_browser/_graphic_items.py:677 calls `toggle_bad(x)`.
  - Epoch toggle: src/mne_qt_browser/_graphic_items.py:601–623 calls `self.weakmain()._toggle_bad_epoch(x)` which returns `(epoch_idx, color)`.
  - If a color is provided (usually the “bad epoch” color from MNE, commonly red), the code constructs a per‑channel RGBA for that epoch and writes it into `self.mne.epoch_color_ref[:, epoch_idx]`.
  - Then every trace refreshes its colors and data (src/mne_qt_browser/_graphic_items.py:629–632). In `update_data()`, segments that don’t match the trace’s active color are masked (set to NaN), making the chosen epoch color dominate the view (src/mne_qt_browser/_graphic_items.py:579–585).

- Where the red comes from conceptually:
  - MNE‑Python’s epoch “bad” color is exposed to the backend (often referred to as `self.mne.epoch_color_bad`) and may default to red. `_toggle_bad_epoch(...)` returns the color to apply; this repo then paints that epoch using the provided color.

- How to change it (options):
  - Change the bad‑epoch color globally before plotting by setting `epoch_color_bad` on the figure params (if exposed), or by customizing MNE’s config so `_toggle_bad_epoch(...)` returns a different color.
  - Provide `epoch_colors` when calling `epochs.plot(...)` to use a custom per‑epoch palette from the start (the backend will honor it when building `epoch_color_ref`): see how `epoch_colors` is used in src/mne_qt_browser/_pg_figure.py:335–348.
  - Disable recoloring on click (browse‑only visual): remove the write to `epoch_color_ref` on toggle.

Minimal change we applied to keep the time‑series colors stable on click

- We changed `DataTrace.toggle_bad(...)` so it no longer modifies `epoch_color_ref` or forces trace recoloring; it only updates the overview bar’s bad‑epoch shading:
  - src/mne_qt_browser/_graphic_items.py:599–606 now calls `_toggle_bad_epoch(x)` and `overview_bar.update_bad_epochs()` and returns early.

Result

- Clicking still toggles the epoch’s state (and the overview bar updates), but the time‑series colors remain unchanged — eliminating the “turn red on click” effect.
