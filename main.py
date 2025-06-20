from graphics import Canvas
import random
from ai import call_gpt
    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    main_screen(canvas)
    #menu(canvas)
    #dna_screen(canvas)
    mouse_click(canvas)


def main_screen(canvas):
    draw_image(canvas,0,0,500,500,"first page.JPEG")
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        print("Clicked at:", x, y)

        # Check if click is inside the START button (150,170,340,230)
        if 150 <= x <= 340 and 170 <= y <= 230:
            canvas.clear()  # Clear menu screen
            instructions(canvas)  # Show new screen
            break  # Exit the loop to prevent repeating

# main menu page
def menu(canvas):
    draw_image(canvas,0,0,500,500,"menu page.JPEG")
      
def instructions(canvas):
    draw_image(canvas,0,0,500,500,"Photoroom_20250606_132005.JPEG")
    #draw_buttons(canvas,185,425,325,480,"salmon")
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        print("Clicked at:", x, y)

        # Check if click is inside the START button (185,425,325,480)
        if 185 <= x <= 325 and 425 <= y <= 480:
            canvas.clear()  # Clear menu screen
            menu(canvas)  # Show new screen
            break  # Exit the loop to prevent repeating

# Main Page title   
def draw_title(canvas,x,y,text,font,font_size,color):
    start_x = x
    start_y = y
    text = canvas.create_text(start_x,start_y,text,font,font_size,color)
    print (text)

# Mouse Clicks
def mouse_click(canvas):
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        print("Clicked at:", x, y)

        # Check if click is inside the DNA button (130,260,370,190)
        if 130 <= x <= 370 and 190 <= y <= 260:
            canvas.clear()  # Clear menu screen
            dna_screen(canvas)  # Show new screen
            break  # Exit the loop to prevent repeating
        
        # Check if click is inside the RNA button (130,345,370,284)
        elif 130 <= x <= 370 and 284 <= y <= 345:
            canvas.clear()  # Clear menu screen
            rna_screen(canvas)  # Show new screen
            break  # Exit the loop to prevent repeating


        # Check if click is inside the PROTEIN button (130,430,370,370)
        elif 130 <= x <= 370 and 370 <= y <= 430:
            canvas.clear()  # Clear menu screen
            protein_screen(canvas)  # Show new screen
            break  # Exit the loop to prevent repeating

# Dna Screen
def dna_screen(canvas):
    draw_image(canvas,0,0,500,500,"background edited.jpg")
    draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
    #draw_image(canvas,10,10,150,150,"Photoroom_20250606_181903.PNG")
    highlights = [] 
    draw_title(canvas, 170, 20, "DNA", "Gill Sans", 70, "#167eabb5")
    draw_title(canvas, 140, 100, "Click on the dna bases to insert" ,"Gill Sans", 16, "salmon")
    draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
    draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
    draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
    #draw_buttons(canvas, 120, 250, 230, 250, "lightblue")  # Back button
    draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
    #draw_buttons(canvas, 150, 350, 350, 400, "#eff2ce8c")  # Back button
    # Generate and store DNA sequences
    sequences = [list(seq) for seq in generate_dna_sequences(3, 10)]

    # Store the top-left coordinates for where to draw each sequence
    sequence_positions = [(50, 180), (50, 230), (50, 280)]
    draw_gap_buttons(canvas, sequence_positions)
    draw_sequences(canvas, sequences, sequence_positions)



    # Interaction loop
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        print("Clicked:", x, y)

        # Back button (10, 430, 50, 470)
        if 10 <= x <= 50 and 430 <= y <= 470:
            canvas.clear()
            menu(canvas)
            mouse_click(canvas)
            break
        

        # Check for gap button clicks
        for i, (start_x, start_y) in enumerate(sequence_positions):
            for j in range(len(sequences[i]) + 1):
                gap_x = start_x + j * 25
                gap_y = start_y - 20
                if gap_x <= x <= gap_x + 20 and gap_y <= y <= gap_y + 20:
                    sequences[i].insert(j, '-')  # Insert gap at position j
                    canvas.clear()
                    draw_image(canvas,0,0,500,500,"background edited.jpg")
                    draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
                    draw_title(canvas, 170, 20, "DNA", "Gill Sans", 70, "#167eabb5")
                    draw_title(canvas, 140, 100, "Click on the dna bases to insert" ,"Gill Sans", 16, "salmon")
                    draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
                    draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
                    draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")  
                    draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
                    draw_gap_buttons(canvas, sequence_positions)
                    draw_sequences(canvas, sequences, sequence_positions,highlights)
                    
        # Check Alignment button clicked (135,250,230,250)150, 350, 350, 400
        if 150 <= x <= 350 and 350 <= y <= 400:
            max_length = max(len(seq) for seq in sequences)
            score = 0

            # Pad sequences with gaps to same length
            padded = []
            for seq in sequences:
                padded.append(seq + ['-'] * (max_length - len(seq)))

            highlights = []
            for col in range(max_length):
                bases = [padded[row][col] for row in range(3)]
                if bases.count(bases[0]) == 3:
                    score += 1
                    highlights.append(col)

            # Redraw screen and show result
            #canvas.clear()
            draw_image(canvas,0,0,500,500,"background edited.jpg")
            draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
            draw_title(canvas, 170, 20, "DNA", "Gill Sans", 70, "#167eabb5")
            draw_title(canvas, 140, 100, "Click on the dna bases to insert" ,"Gill Sans", 16, "salmon")
            draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
            draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
            draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
            draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
            draw_gap_buttons(canvas, sequence_positions)
            draw_sequences(canvas, sequences, sequence_positions,highlights)

            # Show score (122,336,341,340)
            canvas.create_text(120, 320, f"Score: {score}", "Tahoma", 20, "#006f85fc")
            if score == max_length:
                canvas.create_text(205, 320, "Perfect alignment! 🎯", "arial", 20, "#f72f39a3")
            elif score >= 3:
                canvas.create_text(205, 320, "Nice job!", "arial", 20, "#f72f39a3")
            else:
                canvas.create_text(205, 320, "Try aligning more columns!", "arial", 20, "SALMON")
 
        
        # UNDO buttons per sequence row
        # Detect click on UNDO button per row
        for i, (start_x, start_y) in enumerate(sequence_positions):
            undo_x = start_x + 350
            undo_y = start_y - 10
            if undo_x <= x <= undo_x + 60 and undo_y <= y <= undo_y + 30:
                print(f"UNDO clicked for row {i}")
                
                # Remove the last '-' from that sequence (if exists)
                for j in range(len(sequences[i]) - 1, -1, -1):
                    if sequences[i][j] == '-':
                        sequences[i].pop(j)
                        break  # only one gap
            

                # Redraw everything
                canvas.clear()
                draw_image(canvas,0,0,500,500,"background edited.jpg")
                draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
                draw_title(canvas, 170, 20, "DNA", "Gill Sans", 70, "#167eabb5")
                draw_title(canvas, 140, 100, "Click on the dna bases to insert" ,"Gill Sans", 16, "salmon")
                draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
                draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
                draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
                draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")  
                draw_gap_buttons(canvas, sequence_positions)
                draw_sequences(canvas, sequences, sequence_positions,highlights)
                

# Rna Screen
def rna_screen(canvas):
    draw_image(canvas,0,0,500,500,"background edited.jpg")
    draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
    highlights = [] 
    draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
    draw_title(canvas, 140, 100, "Click on the RNA bases to insert" ,"Gill Sans", 16, "salmon")
    draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
    draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
    draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
    draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")

    sequences = [list(seq) for seq in generate_rna_sequences(3, 10)]

    sequence_positions = [(50, 180), (50, 230), (50, 280)]
    draw_gap_buttons(canvas, sequence_positions)
    draw_sequences(canvas, sequences, sequence_positions)


    # Interaction loop
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        print("Clicked:", x, y)

        # Back button (10, 430, 50, 470)
        if 10 <= x <= 50 and 430 <= y <= 470:
            canvas.clear()
            menu(canvas)
            mouse_click(canvas)
            break
        

        # Check for gap button clicks
        for i, (start_x, start_y) in enumerate(sequence_positions):
            for j in range(len(sequences[i]) + 1):
                gap_x = start_x + j * 25
                gap_y = start_y - 20
                if gap_x <= x <= gap_x + 20 and gap_y <= y <= gap_y + 20:
                    sequences[i].insert(j, '-')  # Insert gap at position j
                    canvas.clear()
                    draw_image(canvas,0,0,500,500,"background edited.jpg")
                    draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
                    draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
                    draw_title(canvas, 140, 100, "Click on the RNA bases to insert" ,"Gill Sans", 16, "salmon")
                    draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
                    draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
                    draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
                    
                    draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
                    draw_gap_buttons(canvas, sequence_positions)
                    draw_sequences(canvas, sequences, sequence_positions,highlights)
                    
        # Check Alignment button clicked (135,250,230,250)150, 350, 350, 400
        if 150 <= x <= 350 and 350 <= y <= 400:
            max_length = max(len(seq) for seq in sequences)
            score = 0

            # Pad sequences with gaps to same length
            padded = []
            for seq in sequences:
                padded.append(seq + ['-'] * (max_length - len(seq)))

            highlights = []
            for col in range(max_length):
                bases = [padded[row][col] for row in range(3)]
                if bases.count(bases[0]) == 3:
                    score += 1
                    highlights.append(col)

            # Redraw screen and show result
            #canvas.clear()
            draw_image(canvas,0,0,500,500,"background edited.jpg")
            draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
            draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
            draw_title(canvas, 140, 100, "Click on the RNA bases to insert" ,"Gill Sans", 16, "salmon")
            draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
            draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
            draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
            draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
            draw_gap_buttons(canvas, sequence_positions)
            draw_sequences(canvas, sequences, sequence_positions,highlights)

            # Show score (122,336,341,340)
            canvas.create_text(120, 320, f"Score: {score}", "Tahoma", 20, "#006f85fc")
            if score == max_length:
                canvas.create_text(205, 320, "Perfect alignment! 🎯", "arial", 20, "#f72f39a3")
            elif score >= 3:
                canvas.create_text(205, 320, "Nice job!", "arial", 20, "#f72f39a3")
            else:
                canvas.create_text(205, 320, "Try aligning more columns!", "arial", 20, "SALMON")
 
        
        # UNDO buttons per sequence row
        # Detect click on UNDO button per row
        for i, (start_x, start_y) in enumerate(sequence_positions):
            undo_x = start_x + 350
            undo_y = start_y - 10
            if undo_x <= x <= undo_x + 60 and undo_y <= y <= undo_y + 30:
                print(f"UNDO clicked for row {i}")
                
                # Remove the last '-' from that sequence (if exists)
                for j in range(len(sequences[i]) - 1, -1, -1):
                    if sequences[i][j] == '-':
                        sequences[i].pop(j)
                        break  # only one gap
            

                # Redraw everything
                canvas.clear()
                draw_image(canvas,0,0,500,500,"background edited.jpg")
                draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
                draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
                draw_title(canvas, 140, 100, "Click on the RNA bases to insert" ,"Gill Sans", 16, "salmon")
                draw_title(canvas, 135, 115,"gaps and try to align matching bases", "Gill Sans", 16, "salmon")
                draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
                draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
                draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")  
                draw_gap_buttons(canvas, sequence_positions)
                draw_sequences(canvas, sequences, sequence_positions,highlights)


# Protein Screen
def protein_screen(canvas):
    draw_image(canvas,0,0,500,500,"background edited.jpg")
    draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
    highlights = [] 
    draw_title(canvas, 170, 20, "DNA", "Gill Sans", 70, "#167eabb5")
    draw_title(canvas, 140, 100, "Align the letters by inserting" ,"Gill Sans", 16, "salmon")
    draw_title(canvas, 135, 115,"gaps and match the amino acids", "Gill Sans", 16, "salmon")
    draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
    draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
    draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
    #draw_buttons(canvas, 10, 350, 130, 390, "lightblue")  # Back button
    #draw_title(canvas, 30, 355, "BACK", "arial", 14, "black")

    sequences = [list(seq) for seq in generate_protein_sequences(3, 10)]

    sequence_positions = [(50, 180), (50, 230), (50, 280)]
    draw_gap_buttons(canvas, sequence_positions)
    draw_sequences(canvas, sequences, sequence_positions)


    # Interaction loop
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        print("Clicked:", x, y)

        # Back button (10, 430, 50, 470)
        if 10 <= x <= 50 and 430 <= y <= 470:
            canvas.clear()
            menu(canvas)
            mouse_click(canvas)
            break
        

        # Check for gap button clicks
        for i, (start_x, start_y) in enumerate(sequence_positions):
            for j in range(len(sequences[i]) + 1):
                gap_x = start_x + j * 25
                gap_y = start_y - 20
                if gap_x <= x <= gap_x + 20 and gap_y <= y <= gap_y + 20:
                    sequences[i].insert(j, '-')  # Insert gap at position j
                    canvas.clear()
                    draw_image(canvas,0,0,500,500,"background edited.jpg")
                    draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
                    draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
                    draw_title(canvas, 140, 100, "Align the letters by inserting" ,"Gill Sans", 16, "salmon")
                    draw_title(canvas, 135, 115,"gaps and match the amino acids", "Gill Sans", 16, "salmon")
                    draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
                    draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
                    
                    draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
                    draw_gap_buttons(canvas, sequence_positions)
                    draw_sequences(canvas, sequences, sequence_positions,highlights)
                    
        # Check Alignment button clicked (135,250,230,250)150, 350, 350, 400
        if 150 <= x <= 350 and 350 <= y <= 400:
            max_length = max(len(seq) for seq in sequences)
            score = 0

            # Pad sequences with gaps to same length
            padded = []
            for seq in sequences:
                padded.append(seq + ['-'] * (max_length - len(seq)))

            highlights = []
            for col in range(max_length):
                bases = [padded[row][col] for row in range(3)]
                if bases.count(bases[0]) == 3:
                    score += 1
                    highlights.append(col)

            # Redraw screen and show result
            #canvas.clear()
            draw_image(canvas,0,0,500,500,"background edited.jpg")
            draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
            draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
            draw_title(canvas, 140, 100, "Align the letters by inserting" ,"Gill Sans", 16, "salmon")
            draw_title(canvas, 135, 115,"gaps and match the amino acids", "Gill Sans", 16, "salmon")
            draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
            draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
            draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")
            draw_gap_buttons(canvas, sequence_positions)
            draw_sequences(canvas, sequences, sequence_positions,highlights)

            # Show score (122,336,341,340)
            canvas.create_text(120, 320, f"Score: {score}", "Tahoma", 20, "#006f85fc")
            if score == max_length:
                canvas.create_text(205, 320, "Perfect alignment! 🎯", "arial", 20, "#f72f39a3")
            elif score >= 3:
                canvas.create_text(205, 320, "Nice job!", "arial", 20, "#f72f39a3")
            else:
                canvas.create_text(205, 320, "Try aligning more columns!", "arial", 20, "SALMON")
 
        
        # UNDO buttons per sequence row
        # Detect click on UNDO button per row
        for i, (start_x, start_y) in enumerate(sequence_positions):
            undo_x = start_x + 350
            undo_y = start_y - 10
            if undo_x <= x <= undo_x + 60 and undo_y <= y <= undo_y + 30:
                print(f"UNDO clicked for row {i}")
                
                # Remove the last '-' from that sequence (if exists)
                for j in range(len(sequences[i]) - 1, -1, -1):
                    if sequences[i][j] == '-':
                        sequences[i].pop(j)
                        break  # only one gap
            

                # Redraw everything
                canvas.clear()
                draw_image(canvas,0,0,500,500,"background edited.jpg")
                draw_image(canvas,350,-10,200,150,"Photoroom_20250606_171931.PNG")
                draw_title(canvas, 170, 20, "RNA", "Gill Sans", 70, "#167eabb5")
                draw_title(canvas, 140, 100, "Align the letters by inserting" ,"Gill Sans", 16, "salmon")
                draw_title(canvas, 135, 115,"gaps and match the amino acids", "Gill Sans", 16, "salmon")
                draw_title(canvas, 225, 130,"vertically", "Gill Sans", 16, "salmon")
                draw_image(canvas,135,250,230,250,"Photoroom_20250606_143200.PNG")
                draw_title(canvas, 180, 360, "Check Match", "Gill Sans", 25, "#167eabb5")  
                draw_gap_buttons(canvas, sequence_positions)
                draw_sequences(canvas, sequences, sequence_positions,highlights)


def draw_sequences(canvas, sequences, positions, highlights=None):
    if highlights is None:
        highlights = []  # Ensure it's always defined as a list

    for i, (x, y) in enumerate(positions):
        for j, base in enumerate(sequences[i]):
            base_x = x + j * 25
            base_y = y

            if j in highlights:
                # Highlight matching column
                canvas.create_rectangle(base_x+80 , base_y, base_x+20, base_y, "#ff64457c")

            canvas.create_text(base_x+10, base_y-10, base, "arial", 14, "#007a99fc")

    for i, (x, y) in enumerate(positions):
        for j, base in enumerate(sequences[i]):
            base_x = x + j * 25
            base_y = y 
            if j in highlights:
                canvas.create_rectangle(base_x - 2, base_y - 15, base_x + 20, base_y + 5, "#ff64457c")  # highlight background
            canvas.create_text(base_x+10, base_y-10, base, "arial", 14, "#007a99fc")

def draw_gap_buttons(canvas, positions):
    for row_index, (x, y) in enumerate(positions):
        for i in range(11):  # 10 letters + 1 gap at end
            gap_x = x + i * 25
            gap_y = y - 20
            canvas.create_rectangle(gap_x, gap_y, gap_x + 125 , gap_y + 40, "white","#cfb98277")

            # Add UNDO button to the right of each sequence
            undo_x = x + 300
            undo_y = y - 40
            canvas.create_rectangle(undo_x+80, undo_y+26, undo_x + 143, undo_y + 50, "#feffeda5")
            canvas.create_text(undo_x + 90, undo_y + 30, "Undo", "arial", 16, "#007a99fc")

#buttons
def draw_buttons(canvas,x,y,a,b,color):
    dna = canvas.create_rectangle(x,y,a,b,color)

#Images
def draw_image(canvas,x,y,w,h,f_name):
    left_x = x
    top_y = y
    width = w
    height = h
    filename = f_name
    #image = canvas.create_image(left_x, top_y, filename)
    image = canvas.create_image_with_size(left_x, top_y, width, height, filename)



def generate_dna_sequences(count, length):
    return [''.join(random.choices('ACGT', k=length)) for _ in range(count)]

def generate_rna_sequences(count, length):
    return [''.join(random.choices('ACGU', k=length)) for _ in range(count)]

def generate_protein_sequences(count, length):
    return [''.join(random.choices('DFHIKL', k=length)) for _ in range(count)]

#ACDEFGHIKLMNPQRSTVWY

if __name__ == '__main__':
    main()

