import os
os.environ["OPENAI_API_KEY"] = "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"


from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.