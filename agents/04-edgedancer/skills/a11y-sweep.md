# A11y Sweep

Run a practical accessibility pass on changed screens, components, or workflows.

## When to invoke

- A PR changes forms, modals, navigation, menus, or status feedback.
- A new component library abstraction is being introduced.
- The team wants a concrete accessibility review, not a vague promise.

## Inputs required

- Changed UI files or screens
- Framework or component system in use
- Design notes or expected interactions
- Existing automated accessibility tests, if any

## Procedure

1. Identify the components and user flows affected by the change.
2. Inspect semantics first: element choice, labels, names, descriptions, roles, and error associations.
3. Walk the keyboard path: focus order, focus visibility, escape routes, modal traps, and submit behavior.
4. Check dynamic feedback: live regions, loading states, validation errors, status changes, and announcements.
5. Review motion, timing, and reduced-motion concerns where the UI depends on animation or delayed state.
6. Add or recommend automated checks and manual test cases, then prioritize fixes by severity and frequency.

## Output shape

- Accessibility findings by severity
- Affected flows and components
- Fix recommendations
- Automated tests to add
- Manual verification checklist
