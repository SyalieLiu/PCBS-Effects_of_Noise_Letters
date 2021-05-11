'''
Created on Wed Apr 12 10:19:01 2021

@author: syalie
'''

import random
from expyriment import design, control, stimuli, misc


# terminological precision: "group" means ["H", "K"] or ["S", "C"]
# and "category" means angular or 

def get_other_letter_from_same_group(letter):
    if letter == "H":
        return "K"
    elif letter == "K":
        return "H"
    elif letter == "S":
        return "C"
    elif letter == "C":
        return "S"
    
def get_random_letter_from_other_group(letter):
    if letter in ["H", "K"]:
        return random.sample(["S", "C"], k=1)[0]
    elif letter in ["S", "C"]:
        return random.sample(["H", "K"], k=1)[0]
 
def get_random_letters_from_same_category(letter): 
    angular_letters = ['N', 'W', 'Z']
    curved_letters = ['G', 'J', 'Q']
    if letter in ["H", "K"]:
        random.shuffle(angular_letters)
        return angular_letters
    elif letter in ["S", "C"]:
        random.shuffle(curved_letters)
        return curved_letters    
    
def get_random_letters_from_other_category(letter): 
    angular_letters = ['N', 'W', 'Z']
    curved_letters = ['G', 'J', 'Q']
    if letter in ["S", "C"]:
        random.shuffle(angular_letters)
        return angular_letters
    elif letter in ["H", "K"]:
        random.shuffle(curved_letters)
        return curved_letters
    
    
if __name__ == "__main__":    

    MAX_RESPONSE_DELAY = 2000
    TARGETS = ["H", "K", "S", "C"] * 2  #to change for real experiment
    random.shuffle(TARGETS)
    
    LEFT_RESPONSE = misc.constants.K_l
    RIGHT_RESPONSE = misc.constants.K_r
    
    exp = design.Experiment(name="Noise Letters", text_size=20)
    control.initialize(exp)
    
    cross = stimuli.FixCross(size=(50, 50), line_width=4)
    blankscreen = stimuli.BlankScreen()
    instructions = stimuli.TextScreen("Instructions",
        f"""You'll see a letter at the center of the screen.
        Your task is to decide, as quickly as possible:
        if it is H or K, press 'L'
        if it is S or C, press 'R'
        There will be 6 blocks, and {len(TARGETS)} trials in each block.    
        You must only respond to the letter at the center of the screen
        and ignore any other letter.  
        Press any key to start.""")
    
    # create the stimuli for the trials of each block
    stimuli_block1 = []
    for letter in TARGETS:
        stimuli_block1.append([letter, stimuli.TextLine(letter, text_size = 50)])
    
    random.shuffle(TARGETS)
    
    stimuli_block2 = []
    for letter in TARGETS:
        stim = [letter, stimuli.TextLine(letter, text_size = 50)] 
        for pos in [-250, -200, -150, 150, 200, 250]:
            stim.append(stimuli.TextLine(letter, text_size = 50, position=(pos,0)))           
        stimuli_block2.append(stim)
        
    random.shuffle(TARGETS)
        
    stimuli_block3 = []
    for letter in TARGETS:
        noise_letter = get_other_letter_from_same_group(letter)
        stim = [letter, stimuli.TextLine(letter, text_size = 50)] 
        for pos in [-250, -200, -150, 150, 200, 250]:
            stim.append(stimuli.TextLine(noise_letter, text_size = 50, position=(pos,0)))           
        stimuli_block3.append(stim)     
    
    random.shuffle(TARGETS)
        
    stimuli_block4 = []
    for letter in TARGETS:
        noise_letter = get_random_letter_from_other_group(letter)
        stim = [letter, stimuli.TextLine(letter, text_size = 50)] 
        for pos in [-250, -200, -150, 150, 200, 250]:
            stim.append(stimuli.TextLine(noise_letter, text_size = 50, position=(pos,0)))           
        stimuli_block4.append(stim)
        
    random.shuffle(TARGETS)
        
    stimuli_block5 = []
    for letter in TARGETS:
        noise_letters = get_random_letters_from_same_category(letter)
        stim = [letter, stimuli.TextLine(letter, text_size = 50)] 
        for pos, noise_letter in list(zip([-250, -200, -150, 150, 200, 250], noise_letters * 2)):
            stim.append(stimuli.TextLine(noise_letter, text_size = 50, position=(pos,0)))           
        stimuli_block5.append(stim)
        
    random.shuffle(TARGETS)
    
    stimuli_block6 = []
    for letter in TARGETS:
        noise_letters = get_random_letters_from_other_category(letter)
        stim = [letter, stimuli.TextLine(letter, text_size = 50)] 
        for pos, noise_letter in list(zip([-250, -200, -150, 150, 200, 250], noise_letters * 2)):
            stim.append(stimuli.TextLine(noise_letter, text_size = 50, position=(pos,0)))           
        stimuli_block6.append(stim)   
    
    all_stimuli_blocks = [stimuli_block2, stimuli_block3, stimuli_block4,
                          stimuli_block5, stimuli_block6]
    
    
    # Start of the experiment
    
    exp.add_data_variable_names(['letter', 'respkey', 'RT'])    
    control.start(skip_ready_screen=True)
    instructions.present()
    exp.keyboard.wait()
    
    # block 1
    exp.data.add("Block 1")
    stimuli.TextScreen("Block 1", f"Press any key to start the block 1.").present()
    exp.keyboard.wait()
    
    for t in stimuli_block1:
        blankscreen.present()
        exp.clock.wait(1000)
        cross.present()
        exp.clock.wait(500)
        t[1].present()
        key, rt = exp.keyboard.wait([LEFT_RESPONSE, RIGHT_RESPONSE], duration=MAX_RESPONSE_DELAY)
        exp.data.add([t[0], key, rt])
    
    # next blocks each corresponds to an iteration of the following loop
    for block_number, stimuli_block in list(zip(range(2, 7), all_stimuli_blocks)):
        
        exp.data.add("Block " + str(block_number))
        stimuli.TextScreen("Block " + str(block_number),
            f"Press any key to start the block " + str(block_number) + ".").present()
        exp.keyboard.wait()
        
        for t in stimuli_block:
            blankscreen.present()
            exp.clock.wait(1000)
            cross.present()
            exp.clock.wait(500)
            canvas = stimuli.Canvas(size=(700, 500))
            for i in range(1,8):
                t[i].plot(canvas)
            canvas.present()
            key, rt = exp.keyboard.wait([LEFT_RESPONSE, RIGHT_RESPONSE], duration=MAX_RESPONSE_DELAY)
            try:
                key_name = chr(key)
            except TypeError:
                key_name = "none" #if the subject didn't tpe anything
            exp.data.add([t[0], key_name, rt])
   
    control.end()
