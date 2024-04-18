<script>
  import { Heading } from "flowbite-svelte";

  let apiResults, URL = "http://127.0.0.1:8000/"

  const getApiAsync = (URL) => {
    fetch(URL)
      .then((response) => response.json())
      .then((response) => apiResults = response);
  };

  const handleClick = () => { getApiAsync(URL); }

  $: apiResults;

</script>

<Heading>Pricing</Heading>

<main>
  <button on:click={ handleClick }>GetAPI</button>
  
  <div class="response">{apiResults ? JSON.stringify(apiResults, null, 2) : ""}</div>
</main>