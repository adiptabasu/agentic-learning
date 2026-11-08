# Create handwritten visual notes for a topic

Use this when you want a colorful, handwritten-style PNG page to view and copy into your physical notebook. For detailed Markdown notes intended for a Git repository, use the [study notes guide](14-study-notes.md).

## Ask for a visual summary

Invoke `handwritten-visual-notes` or say:

> Read `skills/handwritten-visual-notes/SKILL.md` and follow it. Make one colorful handwritten-style PNG study sheet for [topic] using the material we covered or this source: [lesson/file/link]. I want to view it and copy it into my notebook. Choose a layout that fits the material, keep it readable, and mark any uncertain connection rather than guessing. Do not save it to Git.

Useful visual elements may include:

- A compact concept map showing how [concepts] relate.
- A flow or cycle with arrows that accurately show the steps.
- A comparison of [A] and [B] with a few memorable labels.
- A worked example with key steps annotated.
- A small color key that stays consistent across the page.

## Improve the result

If it is too crowded or abstract, say what to change:

> Keep the same topic, but reduce this to the five relationships I most need to remember. Define unfamiliar terms and make the arrows or connections explicit.

Or ask for a different representation:

> A map isn't helping me. Turn it into a numbered process with one concrete example.

Check whether the visual reflects what was actually taught. If the diagram adds a relationship that was not established, ask the agent to label it as a hypothesis or remove it.

## Keep the purpose clear

The PNG is a visual reference for hand-copying. It is separate from detailed Markdown study notes. By default it is not written to the learning repo; if you want to keep the image there, specify the exact path and Git policy:

> Save the PNG at [path] in my learning repo. Keep the source material cited. Do not add it to my journal.

After using the notes, tell the agent whether they helped; it can revise them based on what was confusing.
