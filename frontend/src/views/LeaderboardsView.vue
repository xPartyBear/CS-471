<template>
    <div>
        <br>
        <div class="header">
            <button @click="showContent('content1')">Daily</button>
            <button @click="showContent('content2')">Weekly</button>
            <button @click="showContent('content3')">Yearly</button>
            <button @click="showContent('content4')">Lifetime</button>
            <button @click="showContent('content5')">Streak</button>
        </div>


        <div class="content" id="content1" style="display: block;">
            <h1>Daily</h1>
            <div class="box-container">
                <div class="box">Daily data 1</div>
                <div class="box">Daily data 2</div>
                <div class="box">Daily data 3</div>
                <div class="box">Daily data 4</div>
                <div class="box">Daily data 5</div>
            </div>
        </div>
        <div class="content" id="content2" style="display: none;">
            <h1>Weekly</h1>
            <div class="box-container">
                <div class="box">Weekly data 1</div>
                <div class="box">Weekly data 2</div>
                <div class="box">Weekly data 3</div>
                <div class="box">Weekly data 4</div>
                <div class="box">Weekly data 5</div>
            </div>
        </div>
        <div class="content" id="content3" style="display: none;">
            <h1>Yearly</h1>
            <div class="box-container">
                <div class="box">Yearly data 1</div>
                <div class="box">Yearly data 2</div>
                <div class="box">Yearly data 3</div>
                <div class="box">Yearly data 4</div>
                <div class="box">Yearly data 5</div>
            </div>
        </div>
        <div class="content" id="content4" style="display: none;">
            <h1>Lifetime</h1>
            <div class="box-container">
                <div class="box">Lifetime data 1</div>
                <div class="box">Lifetime data 2</div>
                <div class="box">Lifetime data 3</div>
                <div class="box">Lifetime data 4</div>
                <div class="box">Lifetime data 5</div>
            </div>
        </div>
        <div class="content" id="content5" style="display: none;">
            <h1>Streak</h1>
            <div class="box-container">
                <div class="box">Streak data 1</div>
                <div class="box">Streak data 2</div>
                <div class="box">Streak data 3</div>
                <div class="box">Streak data 4</div>
                <div class="box">Streak data 5</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        showContent(contentId) {
            // Hide all content divs
            var contents = document.querySelectorAll('.content');
            contents.forEach(function(content) {
                content.style.display = 'none';
            });

            // Show the selected content div
            var selectedContent = document.getElementById(contentId);
            selectedContent.style.display = 'block';
        }
    }
}
</script>

<style scoped>
        body {
            font-family: Arial, sans-serif;
        }
        .header {
            display: flex;
            justify-content: center;
            padding: 10px;
            background-color: #f8f8f8;
            border-bottom: 1px solid #ddd;
        }
        .header button {
            margin: 0 10px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
        }
        .header button:hover {
            background-color: #0056b3;
        }
        .content {
            text-align: center;
        }
        .box {
            border: 1px solid #ddd;
            padding: 20px;
            margin: 5px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .box-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    </style>