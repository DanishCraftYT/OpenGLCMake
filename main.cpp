#include <iostream>

#include "include/glad/glad.h"
#include "include/GLFW/glfw3.h"

#include "include/ImGUI/imgui.h"
#include "include/ImGUI/imgui_impl_glfw.h"
#include "include/ImGUI/imgui_impl_opengl3.h"

int main() {
    // init's glfw.
    glfwInit();

    // glfw window hints.
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // creates GLFW window and checks if it was successfully created.
    GLFWwindow* window = glfwCreateWindow(800, 600, "LearnOpenGL", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    // makes the glfw window the current context.
    glfwMakeContextCurrent(window);

    // loads Glad.
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    // creates the OpenGL viewport.
    glViewport(0, 0, 800, 600);

    // creates the ImGui context and it's IO.
    ImGui::CreateContext();
    ImGuiIO& io = ImGui::GetIO(); (void)io;

    // sets the ImGui style to dark.
    ImGui::StyleColorsDark();

    // ImGui GLFW & OpenGL init functions.
    ImGui_ImplGlfw_InitForOpenGL(window, true);
    ImGui_ImplOpenGL3_Init("#version 330");

    // render loop.
    while(!glfwWindowShouldClose(window))
    {
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // ImGui NewFrame.
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();

        // Shader Stuff.

        // ImGui window.
        ImGui::Begin("imGui");
        ImGui::Text("YAYAY!");
        ImGui::End();

        // ImGui Render.
        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        glfwSwapBuffers(window);
        glfwPollEvents();    
    }

    // ImGui Shutdown.
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();

    // GLFW Terminate.
    glfwTerminate();  
    return 0;
}
