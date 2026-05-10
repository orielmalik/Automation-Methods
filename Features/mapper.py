class StepMapper:

    def execute(self, step, context):
        if step.startswith("Given"):
            return self._given(step, context)

        if step.startswith("When"):
            return self._when(step, context)

        if step.startswith("Then"):
            return self._then(step, context)

        raise ValueError(f"Unknown step: {step}")

    def _given(self, step, context):

        step = step.lower()

        if "valid input" in step:
            context.mode = "pass"

        elif "empty" in step:
            context.mode = "empty"

        elif "incorrectly" in step or "invalid" in step:
            context.mode = "invalid"

        else:
            raise ValueError(f"Unknown Given step: {step}")

    def _when(self, step, context):

        if "submit" in step:
            context.action = "submit"
        else:
            raise ValueError(f"Unknown When step: {step}")

    def _then(self, step, context):
        if "redirected" in step:
            context.expect = "success"

        elif "error" in step:
            context.expect = "error"
        else:
            raise ValueError(f"Unknown Then step: {step}")
