<script>
  import { Heading } from "flowbite-svelte";
  // import images from './imageData/images.json';
  import { Carousel, Thumbnails } from 'flowbite-svelte';

  let index = 0;
  let forward = true;

  let apiResults, URL = "http://127.0.0.1:8000/data"
  // This one works: https://api.themoviedb.org/3/trending/tv/week/

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
<!-- 
<div class="max-w-4xl space-y-4">
  <Carousel {images} {forward} let:Indicators let:Controls bind:index>
    <Controls />
    <Indicators />
  </Carousel>
  <Thumbnails {images} {forward} bind:index />
</div> -->