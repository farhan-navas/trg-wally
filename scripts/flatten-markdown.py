# this script flattens a markdown file by removing all newlines and replacing them with '/n'

def flatten_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    return '/n'.join(lines)

if __name__ == '__main__':
    sample_md = """\
I hear how painful this pattern has been for you—always the “big sister” expected to cope on your own while your brother’s struggles get all the attention. That kind of childhood message (“your needs don’t matter as much”) can leave you feeling hurt, resentful, and invisible. Let’s look at some ways to begin shifting those family dynamics and honouring your own needs.

---

### 1. Name and validate the old story

* **Acknowledge the pattern**: “You’ve grown up feeling like your own hurts weren’t worth noticing.”
* **Own your feelings**: It’s okay to be angry, sad, or disappointed about the unfairness you experienced.

### 2. Reframe expectations of your parents

* Your parents’ reflex to rush to your brother doesn’t necessarily mean they love you less—it may just be an overlearned caretaking script.
* By recognizing it as a habit rather than a judgment on your worth, you can start to detach your self-value from their reactions.

### 3. Communicate your needs directly

* **Choose one parent at a time**, and a calm moment:

* “I wanted to share how overlooked I felt growing up when you focused on [Brother]. It still stings.”
* Focus on **“I” statements**: “I need you to hear me and acknowledge my pain, too.”
* **Be specific**: Give an example (“When I had [X crisis], I felt alone. That pattern makes today’s hurt even sharper.”)

### 4. Set compassionate boundaries

* If you start to feel dismissed mid-conversation:

* “I’m becoming upset. Can we pause and try again later?”
* This models for them how to respect your emotional limits.
* Decide what support you want: an apology? a listening ear? practical help? Articulate it.

### 5. Enlist an ally or neutral third party

* A **family therapist** or mediator can gently point out these long-standing patterns and help everyone learn to listen equitably.
* If your parents resist therapy, consider talking first with a close cousin, aunt/uncle, or family friend who understands both sides and can advocate for you.

### 6. Lean into your own support network

* Cultivate friendships or support groups where **your feelings do matter**—let them celebrate you for “figuring things out,” but also hear and hold your pain.
* Journaling, coaching, or a therapist for yourself can help unpack decades of being the “resilient one.”

### 7. Practice self-compassion rituals

* When old stories surface (“I shouldn’t complain because I’m the strong child”), counter with:

* “It’s okay to lean on others, even if I’ve been the helper for so long.”
* Daily reminders: a mantra, a small treat, a grounding breath practice.

---

**Remember:** rewiring a family dynamic takes time and repeated gentle corrections. By naming the old script, speaking your truth, and inviting your parents into a new way of relating, you’ll gradually shift the balance—so that your hurts get the care they deserve, too. You absolutely deserve to be seen and supported.
"""

    flattened = flatten_markdown(sample_md)
    print(flattened)