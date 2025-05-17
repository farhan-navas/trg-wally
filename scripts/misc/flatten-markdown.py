# this script flattens a markdown file by removing all newlines and replacing them with '/n'

def flatten_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    return '/n'.join(lines)

if __name__ == '__main__':
    sample_md = """\
Hey, I’m really sorry you’re going through this. It sounds like you care a lot about him, but these “rules” are crossing into controlling territory—and that’s a red flag. Here’s what I’d think about:

1. **Respect and Trust**

   * Healthy relationships are built on mutual trust, not bans and policing.
   * If he truly trusted you, he wouldn’t demand you cut off lifelong friendships or constantly check up on you.

2. **Your Autonomy**

   * You have the right to decide who you spend time with, what you wear, and when you come home.
   * If you feel your freedom slipping away, it’s a sign you’re losing yourself in this relationship.

3. **Double Standards and Misogyny**

   * Calling other women “whores” and shaming you for the way you dress shows a lack of respect for women in general—including you.
   * That mindset doesn’t just disappear once you move in together; it often gets worse behind closed doors.

4. **His “Protection” vs. Control**

   * It’s valid to worry about safety in your city—but forbidding everything isn’t protection, it’s control.
   * If he truly cared, he’d help you find safe ways to get home (ride-share apps, travelling in groups) instead of setting curfews.

5. **Weighing the “Good”**

   * Financial support and kindness are wonderful—but they shouldn’t come at the cost of your independence and self-respect.
   * Ask yourself: Will you feel valued or suffocated in the long term?

---

**What you can do next**

* **Have a heart-to-heart**: Tell him calmly how these rules make you feel. Real change only comes if he’s willing to listen and adjust.
* **Set clear boundaries**: If he can’t respect your friendships, your choices, or your body autonomy, that boundary might need to be “I’ll walk away.”
* **Lean on your support network**: Talk to friends or family you trust about what’s happening—they can remind you what a healthy relationship looks like.
* **Consider your future**: A partner should lift you up, not tie you down. If you can’t imagine feeling free and respected, it might be time to break up.

At the end of the day, you deserve someone who trusts you completely, respects your choices, and treats you as an equal. If he can’t meet you there, it’s not you—it’s the relationship. 💛

"""

    flattened = flatten_markdown(sample_md)
    print(flattened)