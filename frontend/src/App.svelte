<script>
  let article = "";
  let summary = "";

  async function summarize() {
    try {
      const response = await fetch("http://localhost:8000/summary", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-API-KEY": "c674d8bc-15e7-4fd4-8a3f-6a5ddbdb9226",
        },
        body: JSON.stringify({ article: article }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      summary = await response.text();
    } catch (error) {
      console.error("Error:", error);
      summary = "Failed to fetch answer.";
    }
  }
</script>

<main>
  <h1>Summarize an article</h1>
  <div class="input-container">
    <textarea bind:value={article} placeholder="Type your article here" />
    <button on:click={summarize}>Summarize</button>
  </div>
  <pre>{summary}</pre>
</main>

<style>
  main {
    text-align: center;
    padding: 50px;
    font-family: Arial, sans-serif;
  }
  textarea,
  button {
    font-size: 1.2rem;
    padding: 0.5rem;
    margin: 0.5rem;
  }
  textarea {
    width: 800px;
    height: 200px;
  }
  button {
    cursor: pointer;
  }
  pre {
    max-width: 100%;
    white-space: break-spaces;
    text-align: left;
  }
  .input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  button {
    width: 200px; /* Set a fixed width for the button */
  }
</style>
