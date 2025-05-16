# this script flattens a markdown file by removing all newlines and replacing them with '/n'

def flatten_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    return '/n'.join(lines)

if __name__ == '__main__':
    sample_md = """\
Hey dear, it sounds like she’s feeling overlooked and wants more of your attention. Let’s break down a way to approach this:

---

**1. Acknowledge her feelings**

> “I see that you’ve been feeling like you’re not the center of my world right now, and that must be tough.”

This shows you recognize her experience without minimizing it.

**2. Reflect on what she needs**
Ask her directly:

> “Can you tell me what makes you feel most valued and seen?”

Maybe she needs more one-on-one time, verbal appreciation, or little gestures throughout the day.

**3. Share your intentions**
Let her know:

> “I care about you deeply. It wasn’t my intention to make you feel second-place—sometimes I get caught up in other things and forget how important this is.”

Owning that oversight can go a long way.

**4. Co-create simple rituals**
Brainstorm small but meaningful ways to show focus—like a daily “15-minute check-in,” surprise notes, or planning a mini date. Framing it together as something you both look forward to keeps it collaborative.

**5. Keep checking in**
After you try some of these rituals, circle back:

> “How are you feeling about our check-ins? Is there anything I can do to make them more special?”

This ongoing feedback loop prevents old patterns from sneaking back in.

---

By validating her feelings, asking what she truly needs, and then following through with small, consistent actions, you’ll help her feel genuinely valued—without turning every moment into a spotlight, but by building shared moments of connection.
"""

    flattened = flatten_markdown(sample_md)
    print(flattened)