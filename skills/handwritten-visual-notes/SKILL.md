---
name: handwritten-visual-notes
description: Create colorful handwritten-style visual study sheets that the learner can view and copy into a physical notebook.
---
# Handwritten visual notes

Use this skill when the learner wants to see a memorable visual page and reproduce it by hand. For detailed Markdown notes intended for a Git repository, use `skills/study-notes/SKILL.md` instead.

## Create a visual sheet

- Confirm the topic, source material, audience level if relevant, and how much material should fit on the page.
- Before choosing colors, check the project-root `HANDWRITTEN-VISUAL-NOTES-PALETTE.md` for saved preferences. Use configured values without asking the learner to repeat them; explicit palette instructions in the current request take precedence for that page. If a value is blank or the file is missing, use a restrained, harmonious default for that value.
- Use confirmed lesson content or trusted sources. Flag uncertainty rather than inventing a relationship or fact to make the page look complete.
- Produce a full-color PNG by default. Use a clear handwritten-note aesthetic, strong visual hierarchy, a small consistent color palette, readable labels, arrows or diagrams that show real relationships, a useful example, and enough whitespace to copy the page.
- Honor any palette or color preferences the learner gives. Support preferences for the page background, body text, headings, highlights, and diagram accents such as arrows or labels. If no preference is given and no saved preference exists, choose a restrained, harmonious palette and proceed; optionally mention that colors can be saved in the project palette file for future pages.
- Keep text and highlights legible against the page background, and use a limited set of colors that is practical to reproduce by hand. Avoid using color alone to communicate meaning; pair it with labels, shapes, or line styles where useful.
- Keep each page focused on one small topic chunk. Split dense material into multiple pages rather than shrinking text or crowding the layout.
- Include a concise text description for accessibility. Ask whether the visual helped and refine it from learner feedback.
- If no image-generation or rendering capability is available, say so plainly and offer a structured visual layout the learner can draw. Do not claim to have created a PNG when none exists.

## Finish the visual-notes mode

When the learner asks to finish or turn this mode off, consolidate the current sheet(s), review text accuracy and legibility, and show the PNG or a clear description for review. The default purpose is copying by hand; do not save the PNG in a Git workspace unless the learner separately asks and agrees on the exact path and tracking policy. Then state that the mode is closed.
