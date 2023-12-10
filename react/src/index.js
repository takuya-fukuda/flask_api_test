import React from 'react';
//import ReactDOM from 'react-dom';
import ReactDOM from 'react-dom/client'
import API_URL from './App.js'; // APIのURLをインポート

class YourReactComponent extends React.Component {
  handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        body: formData,
      });
      const blob = await response.blob();

      const resultImage = document.getElementById('resultImage');
      resultImage.src = URL.createObjectURL(blob);
      resultImage.style.display = 'block';
    } catch (error) {
      console.error('APIリクエストエラー:', error);
    }
  };

  previewFile = (input) => {
    const fileReader = new FileReader();
    fileReader.onload = function () {
      const preview = document.getElementById('preview');
      preview.src = fileReader.result;
    };
    fileReader.readAsDataURL(input.target.files[0]);
  };

  render() {
    return (
      <div>
        {/* 画像コンテナ */}
        <div className="image-container">
          <img id="preview" src="https://placehold.jp/x150.png" alt="" />
          <img id="resultImage" src="https://placehold.jp/x150.png" style={{ display: 'none' }} alt=""/>
        </div>

        {/* フォーム */}
        <form onSubmit={this.handleSubmit} encType="multipart/form-data">
          <p>
            <input type="file" name="file" accept="image/*" onChange={(e) => this.previewFile(e)} />
          </p>
          <input type="submit" value="AI判定" />
        </form>
      </div>
    );
  }
}

const root = document.getElementById('root');
const reactRoot = ReactDOM.createRoot(root);
reactRoot.render(<YourReactComponent />);

//ReactDOM.render(
//  <YourReactComponent />,
//  document.getElementById('root')
//);
