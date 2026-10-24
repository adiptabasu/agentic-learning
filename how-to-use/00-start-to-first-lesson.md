# From a learning goal to your first lesson

Use this walkthrough when you have something you want to learn or prepare for and want help turning it into a realistic plan and a first teaching session. Replace bracketed text with your details. It is fine to say “I don't know yet.”

## 1. Start with the Learning Guide

Invoke the `learning-guide` skill if your agent provides a shortcut. Otherwise, paste:

> Read `skills/learning-guide/SKILL.md` and follow it. I want to prepare for [exam, role, subject, project, or other goal]. Help me clarify what I need to learn and whether this goal is realistic. Ask one focused question at a time. Do not make a learning plan until we understand my starting point, constraints, and what success means.

For example:

> Read `skills/learning-guide/SKILL.md` and follow it. I want to prepare for a junior data analyst role, but I'm not sure what skills I need or whether I'm ready to start. Help me work that out. Ask one question at a time, and don't assume what I already know.

Answer honestly. If you are unsure, say so; the guide should help explore the uncertainty rather than force a choice. Mention relevant facts such as prior experience, time available, location, budget, deadlines, or accessibility needs when they matter to your goal.

## 2. Clarify until the goal is understood

The Learning Guide should ask about your motivation, what you know or have tried, constraints, and what would count as success. If it starts prescribing a course before understanding those things, steer it back:

> Before recommending a route, please clarify my current level, constraints, and what outcome I actually need. Ask me the next most useful question.

When it summarizes your situation, check it carefully. Correct anything inaccurate or missing. Use:

> Your summary is [accurate / partly accurate]. Please correct it as follows: [correction]. Keep facts separate from assumptions and unknowns.

Do not move to planning until you agree the summary represents your goal and starting point.

## 3. Ask for a plan

Once the goal and summary are right, say:

> That summary is accurate. Use the `learning-plan` skill to propose a structured route toward [success criteria]. Include prerequisites, ordered topics, practice, milestones, evidence that will show progress, and review points. Consider [time available, deadline, or other constraints]. Label estimates and uncertainties, and tell me if the target looks unrealistic.

If shortcuts are unavailable, add:

> Read `skills/learning-plan/SKILL.md` and follow it.

Review the route. Ask for changes if the scope, pace, order, or workload does not fit. For example:

> This is too much for the time I have. Revise it for [hours per week] and prioritize the skills most directly tied to [goal]. Explain what will be left out.

When the plan is right, confirm it explicitly:

> I agree to this plan. Treat it as our current plan. Prepare a handoff with my goal, starting point, constraints, success criteria, plan, first milestone, and anything still uncertain.

If you do not agree with the plan yet, continue revising it rather than treating it as settled.

## 4. Hand off to the Teacher

Start the `teacher` skill and provide the confirmed handoff. For example:

> Read `skills/teacher/SKILL.md` and follow it using the confirmed handoff and plan above. I prefer [examples, exercises, discussion, visual explanations, or a mix]. I have [time] for this session. Start with the first milestone, teach one useful chunk at a time, and check my understanding before moving on.

If the handoff is not available in the current chat, paste the confirmed goal and plan or point the Teacher to their agreed location. Do not assume a separate agent can see another chat's history.

## 5. End the session and decide whether to save progress

At the end, ask:

> Summarize what we covered, what I demonstrated that I understand, what remains unclear, and the next step. Do not claim I mastered something unless the evidence supports it.

If you want a journal or a record that will let another agent resume after a clone or pull, first agree on its location, contents, and Git tracking policy. Then ask the agent to use the `progress-journal` skill and update the agreed files for your review. If you want only a one-off lesson, skip the journal; it is optional.

## What the full flow looks like

**Learning Guide → your correction and confirmation → Learning Plan → your approval → Teacher → optional reviewed progress record.** You remain in control at each handoff. The agent should ask rather than assume, and the plan is not settled until you agree to it.
