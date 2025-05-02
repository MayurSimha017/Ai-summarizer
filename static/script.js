async function summarize() {
  const text = document.getElementById("text-input").value;
  const url = document.getElementById("url-input").value;
  const length = document.getElementById("length").value.toLowerCase();
  const style = document.getElementById("style").value;
  const file = document.getElementById("file-input").files[0];

  const formData = new FormData();
  formData.append("text", text);
  formData.append("url", url);
  formData.append("length", length);
  formData.append("style", style);
  if (file) formData.append("file", file);

  const response = await fetch("http://127.0.0.1:5000/summarize", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  document.getElementById("output").innerText = data.summary;
}
