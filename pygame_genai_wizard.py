# pygame_genai_wizard.py
import pygame
import pygame.locals as pl
from tkinter import Tk, filedialog
# TODO - Connect to src\dspygen\rm\chatgpt_codemaster_retriever.py or existing RAG

pygame.init()

# Define some constants
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
BLACK = (0, 0, 0)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wizard Example')

# Define a basic font
font = pygame.font.Font(None, 36)

class WizardPage:
    def __init__(self, title="", subtitle=""):
        self.title = title
        self.subtitle = subtitle
        self.is_valid = True
        self.elements = []

    def render(self, screen):
        screen.fill(WHITE)
        title_surface = font.render(self.title, True, BLUE)
        subtitle_surface = font.render(self.subtitle, True, BLACK)
        screen.blit(title_surface, (20, 20))
        screen.blit(subtitle_surface, (20, 60))
        for element in self.elements:
            element.render(screen)
    
    def add_element(self, element):
        self.elements.append(element)
    
    def initialize_page(self):
        pass

    def validate_page(self):
        return self.is_valid

    def elements_handle_event(self, event):
        for element in self.elements:
            element.handle_event(event)


class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.rect = pygame.Rect(pos[0], pos[1], 200, 50)
    
    def render(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


class RadioButton:
    def __init__(self, text, pos, group, callback=None):
        self.text = text
        self.pos = pos
        self.group = group
        self.callback = callback
        self.rect = pygame.Rect(pos[0], pos[1], 200, 30)
        self.selected = False
        self.group.append(self)
    
    def render(self, screen):
        color = BLUE if self.selected else BLACK
        pygame.draw.circle(screen, color, (self.rect.x + 15, self.rect.y + 15), 10)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 30, self.rect.y))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                for button in self.group:
                    button.selected = False
                self.selected = True
                if self.callback:
                    self.callback(self.selected)


class TextBox:
    def __init__(self, pos, width, height):
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.text = ""
        self.active = False

    def render(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode


class ExamplePage1(WizardPage):
    def __init__(self):
        super().__init__("Welcome to the Example Wizard", "This wizard will guide you through the process of importing data.")
    
    def initialize_page(self):
        print("ExamplePage1 initialized")
        super().initialize_page()

    def validate_page(self):
        print("ExamplePage1 validated")
        return super().validate_page()


class ExamplePage2(WizardPage):
    def __init__(self):
        super().__init__("Select Sources of code_snippets/chat conv", "Select source of code_snippets/chat conv (RAG-url, folder, file)")
        self.radio_group = []
        self.clipboard_rb = RadioButton("Clipboard", (20, 120), self.radio_group)
        self.file_rb = RadioButton("File", (20, 160), self.radio_group, self.file_rb_toggled)
        self.file_btn = Button("Browse...", (340, 150), self.browse_file)

        self.file_le = TextBox((20, 220), 600, 30)
        self.add_element(self.clipboard_rb)
        self.add_element(self.file_rb)
        self.add_element(self.file_le)
        self.add_element(self.file_btn)

    def initialize_page(self):
        print("ExamplePage2 initialized")
        super().initialize_page()

    def file_rb_toggled(self, checked):
        self.file_le.active = checked
        self.file_btn.rect.width = 200 if checked else 0

    def browse_file(self):
        root = Tk()
        root.withdraw()
        file_name = filedialog.askopenfilename(
            title="Select the File or RAG Folder to Import",
            filetypes=(("CSV Files", "*.csv"), ("Text Files", "*.txt"), ("All Files", "*.*")),
        )
        if file_name:
            self.file_le.text = file_name

    def validate_page(self):
        if self.file_rb.selected and not self.file_le.text:
            print("Error: Please select the file to import.")
            return False
        return True


class Wizard:
    def __init__(self):
        self.pages = []
        self.current_page_index = 0

        self.back_button = Button("Back", (20, SCREEN_HEIGHT - 70), self.go_to_previous_page)
        self.next_button = Button("Next", (240, SCREEN_HEIGHT - 70), self.go_to_next_page)
        self.finish_button = Button("Finish", (460, SCREEN_HEIGHT - 70), self.finish)
        self.cancel_button = Button("Cancel", (680, SCREEN_HEIGHT - 70), self.cancel)

    def add_page(self, page, last_page=False):
        self.pages.append(page)
        if last_page:
            self.pages[0].initialize_page()

    def render(self, screen):
        self.pages[self.current_page_index].render(screen)
        if self.current_page_index > 0:
            self.back_button.render(screen)
        if self.current_page_index < len(self.pages) - 1:
            self.next_button.render(screen)
        if self.current_page_index == len(self.pages) - 1:
            self.finish_button.render(screen)
        self.cancel_button.render(screen)

    def handle_event(self, event):
        if self.current_page_index > 0:
            self.back_button.handle_event(event)
        if self.current_page_index < len(self.pages) - 1:
            self.next_button.handle_event(event)
        if self.current_page_index == len(self.pages) - 1:
            self.finish_button.handle_event(event)
        self.cancel_button.handle_event(event)
        self.pages[self.current_page_index].elements_handle_event(event)

    def go_to_previous_page(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1

    def go_to_next_page(self):
        if self.pages[self.current_page_index].validate_page():
            self.current_page_index += 1
            self.pages[self.current_page_index].initialize_page()

    def finish(self):
        if self.pages[self.current_page_index].validate_page():
            print("Wizard finished successfully!")
            pygame.quit()
            exit()

    def cancel(self):
        print("Wizard canceled.")
        pygame.quit()
        exit()


class ExampleWizard(Wizard):
    def __init__(self):
        super().__init__()
        self.add_page(ExamplePage1())
        self.add_page(ExamplePage2(), last_page=True)
        self.add_page(ExamplePage2(), last_page=True)


def test_example_wizard():
    wizard = ExampleWizard()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                running = False
            wizard.handle_event(event)
        
        wizard.render(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    test_example_wizard()
