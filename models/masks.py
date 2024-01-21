"""Mathy utility functions."""
import jax
import jax.numpy as jnp
import numpy as np

def get_freq_reg_mask(pos_enc_length, current_iter, total_reg_iter, max_visible=None, type='submission'):
  '''
  Returns a frequency mask for position encoding in NeRF.
  
  Args:
    pos_enc_length (int): Length of the position encoding.
    current_iter (int): Current iteration step.
    total_reg_iter (int): Total number of regularization iterations.
    max_visible (float, optional): Maximum visible range of the mask. Default is None. 
      For the demonstration study in the paper.
    
    Correspond to FreeNeRF paper:
      L: pos_enc_length
      t: current_iter
      T: total_iter
  
  Returns:
    jnp.array: Computed frequency or visibility mask.
  '''
  if max_visible is None:
    # default FreeNeRF
    if current_iter < total_reg_iter:
      freq_mask = np.zeros(pos_enc_length)  # all invisible
      ptr = pos_enc_length / 3 * current_iter / total_reg_iter + 1 
      ptr = ptr if ptr < pos_enc_length / 3 else pos_enc_length / 3
      int_ptr = int(ptr)
      freq_mask[: int_ptr * 3] = 1.0  # assign the integer part
      freq_mask[int_ptr * 3 : int_ptr * 3 + 3] = (ptr - int_ptr)  # assign the fractional part
      return jnp.clip(jnp.array(freq_mask), 1e-8, 1-1e-8)  # for numerical stability
    else:
      return jnp.ones(pos_enc_length)
  else:
    # For the ablation study that controls the maximum visible range of frequency spectrum
    freq_mask = np.zeros(pos_enc_length)
    freq_mask[: int(pos_enc_length * max_visible)] = 1.0
    return jnp.array(freq_mask)