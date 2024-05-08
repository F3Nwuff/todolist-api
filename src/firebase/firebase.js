// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getFirestore} from "firebase/firestore"
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBDCIEwoh0aOw0bbc3oF4rNeiU50b9Nlf0",
  authDomain: "api-todo-42f3a.firebaseapp.com",
  projectId: "api-todo-42f3a",
  storageBucket: "api-todo-42f3a.appspot.com",
  messagingSenderId: "818931857433",
  appId: "1:818931857433:web:11f4e77dc5e76368d05288"
};



// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const db = getFirestore(app)
export const auth = getAuth(app);