<script>
    import { Label, Input, Heading, Button, P } from 'flowbite-svelte';
    import { onMount } from "svelte"

    /* Purchase / Pricing page:
        - What we offer
        - The prices
        - How to pay
            - Stripe (?)
    */

    let email;
    let password;

    async function sendLoginInfo(email, password) {
        try {
            const url = "http://localhost:8000/login/" + email + "/" + password;
            const res = await fetch(url);
            if (!res.ok) {
                throw new Error("Login fetching didn't work");
            }
            const resData = await res.json();
            email = resData["email"];
            console.log("Email: " + email);
            password = resData["password"];
            console.log("Password: " + password);
        } catch (error) {
            console.log("Error retrieving login info: ", error);
        }
    }
</script>

<Heading><center>Purchase</center></Heading>

<div class="formcontainer">
    <form on:submit|preventDefault={() => {
        try {
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;
            sendLoginInfo(email, password);
        } catch (error) { console.error("Didn't work: ", error); }
    }} class="mainform">
        <Label for="email" class="labels block mb-2">Email</Label>
        <Input id="email" name="email" placeholder="example@example.com" class="inputs"/>
        <Label for="password" class="labels block mb-2">Password</Label>
        <Input id="password" name="password" placeholder="123456789" class="inputs"/> 
        <br>
        <Button type="submit">Sign Up</Button>
    </form>
</div>

<style>
    .formcontainer {
        max-width: 30%;
        margin: auto;
        height: 100vh;
        /* border: 1px solid green; */
    }
</style>
