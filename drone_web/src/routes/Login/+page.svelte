<script>
    import { Label, Input, Heading, Button } from 'flowbite-svelte';
    import { onMount } from "svelte"

    let data;
    let error;

    async function fetchData() {
        try {
            const response = await fetch('http://localhost:8000/data');
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            const responseData = await response.json();
            console.log(response);
            console.log(responseData["message"]);
            data = responseData["message"];
        } catch (error) {
            console.error('Error fetching data:', error);
            error = 'Failed to fetch data. Please try again later.';
        }
    }

    onMount(fetchData);

</script>

<style>
    .formcontainer {
        max-width: 30%;
        margin: auto;
        height: 100vh;
        /* border: 1px solid green; */
    }
</style>

<Heading><center>Log In</center></Heading>

<h1>FastAPI Backend Data:</h1>
  {#if data}
    <p>{data}</p>
  {:else}
    <p>Loading...</p>
  {/if}

<div class="formcontainer">
    <form action="/" class="mainform">
        <Label for="default-input" class="labels block mb-2">Email</Label>
        <Input id="default-input" placeholder="example@example.com" class="inputs"/>
        <Label for="default-input" class="labels block mb-2">Password</Label>
        <Input id="default-input" placeholder="123456789" class="inputs"/> 
        <br>
        <Button type="submit">Log In</Button>
    </form>
</div>