// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBV07R6bkQWL2cELW5CsXyKhFKC7OzBMbU",
  authDomain: "dronewebsite-b308d.firebaseapp.com",
  projectId: "dronewebsite-b308d",
  storageBucket: "dronewebsite-b308d.appspot.com",
  messagingSenderId: "570527511943",
  appId: "1:570527511943:web:fa8655130d4c13dcbe4f22",
  measurementId: "G-MBRDJQRQ4E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);