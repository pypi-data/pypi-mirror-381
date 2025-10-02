# AgentHub SDK

Simple interface to make agents runnable on AgentHub.

## Installation

Add `agenthub_sdk` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:agenthub_sdk, "~> 1.0.2"}
  ]
end
```

## Usage

The AgentHub SDK provides a simple behavior for creating agent runners that can be executed on the AgentHub platform.

### Creating an Agent

To create an agent, implement the `AgenthubSdk` behavior:

```elixir
defmodule MyAgent do
  @behaviour AgenthubSdk

  def run(input) do
    # Process the input and return a result
    {:ok, %{result: "processed", input: input}}
  end
end
```

### Running an Agent

Use `AgenthubSdk.run/2` to execute your agent:

```elixir
result = AgenthubSdk.run(MyAgent, %{data: "test"})
case result do
  {:ok, output} -> IO.puts("Success: #{inspect(output)}")
  {:error, reason} -> IO.puts("Error: #{inspect(reason)}")
end
```

## API Reference

### `AgenthubSdk.run/2`

Runs an agent with the given input.

**Parameters:**
- `agent_module` - The module implementing the AgentRunner behavior
- `input` - The input data to pass to the agent

**Returns:**
- `{:ok, result}` - On successful execution
- `{:error, reason}` - On failure

### Behavior Callback

Your agent module must implement:

```elixir
@callback run(input :: any()) :: {:ok, any()} | {:error, any()}
```

## License

ISC