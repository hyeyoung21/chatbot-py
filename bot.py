from botbuilder.core import ActivityHandler, TurnContext

class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        await turn_context.send_activity(f"🙋‍♂️ 당신이 보낸 메시지: '{user_input}'")