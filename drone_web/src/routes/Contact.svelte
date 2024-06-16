<script>
  import { Section, Contact } from "flowbite-svelte-blocks";
  import { Label, Input, Textarea, Button } from "flowbite-svelte";

  let email_sender;
  let subject;
  let body;

  async function sendEmail(email_sender, subject, body) {
      try {
          const url = "http://localhost:8000/email/" + email_sender + "/" + subject + "/" + body;
          console.log("Fetching");
          const res = await fetch(url);
          console.log("Fetch complete");
          if (!res.ok) {
              throw new Error("Fetching didn't work");
          }
          const resData = await res.json();
          email_sender = resData["email_sender"];
          subject = resData["subject"];
          body = resData["body"];
          const worked = resData["worked"];
          console.log("email_sender: " + email_sender);
          console.log("subject: " + subject);
          console.log("body: " + body);
          console.log("Email sending " + worked);
      } catch (error) {
          console.log("Error retrieving login info: ", error);
      }
  }
</script>
    
<Section name="contact">
  <Contact>
    <svelte:fragment slot="h2">Contact Us</svelte:fragment>
    <svelte:fragment slot="paragraph">Pricing depends on the job, fill out this form and let us know what you would be interested in!</svelte:fragment>
    <form on:submit|preventDefault={() => {
      try {
        const email_sender = document.getElementById("email_sender").value;
        const subject = document.getElementById("subject").value;
        const body = document.getElementById("body").value;
        sendEmail(email_sender, subject, body);
        // Call a function that clears the input and sends a success message (Alert prob)
      } catch (error) { console.error("Didn't work: ", error); }
    }} class="space-y-8">
      <div>
        <Label for="email" class="block mb-2">Your email</Label>
        <Input id="email_sender" name="email" placeholder="name@flowbite.com" required />
      </div>
      <div>
        <Label for="subject" class="block mb-2">Subject</Label>
        <Input id="subject" name="subject" placeholder="Let us know how we can help you" required />
      </div>
      <div>
        <Label for="subject">Message</Label>
        <Textarea id="body" name="body" placeholder="Leave a comment..." label="Your message" />
      </div>
      <Button type="submit">Send message</Button>
    </form>
  </Contact>
</Section>
