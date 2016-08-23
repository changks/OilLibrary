'''
    The oil properties for the sample oil named benzene
    (Note: we put these things in their own separate file because
           some oil properties records can get quite large)
'''

json_data = {'name': 'benzene',
             'api': 28.6,
             'saturates_fraction': 0.0,
             'aromatics_fraction': 1.0,
             'resins_fraction': 0.0,
             'asphaltenes_fraction': 0.0,
             'benzene_fraction': 1.0,
             'polars_fraction': 0.0,
             'naphthenes_fraction': 0.0,
             'sulphur_fraction': 0.0,
             'paraffins_fraction': 0.0,
             'wax_content_fraction': 0.0,
             'pour_point_min_k': 278.68,
             'pour_point_max_k': None,
             'flash_point_min_k': 262.1,
             'flash_point_max_k': None,
             # 'bullwinkle_fraction': None,
             # 'bullwinkle_time': None,
             # 'emulsion_water_fraction_max': None,
             'oil_water_interfacial_tension_n_m': 0.035,
             'oil_water_interfacial_tension_ref_temp_k': 293.15,
             # 'oil_seawater_interfacial_tension_n_m': None,
             # 'oil_seawater_interfacial_tension_ref_temp_k': None,
             # 'adhesion_kg_m_2': None,
             # (Note: for solubility, I would kinda expect volume/volume units,
             #        but Bill's estimation doc uses kg/m^3.)
             'solubility': 1.78,  # kg/m^3
             'nickel_ppm': None,
             'vanadium_ppm': None,
             'k0y': None,
             'cuts': [{'liquid_temp_k': 353.05,
                       'vapor_temp_k': 353.45,
                       'fraction': 1.0
                       },
                      ],
             'densities': [
                           {'kg_m_3': 886.30, 'ref_temp_k': 285.93},
                           {'kg_m_3': 883.26, 'ref_temp_k': 288.71},
                           {'kg_m_3': 880.37, 'ref_temp_k': 291.48},
                           {'kg_m_3': 877.33, 'ref_temp_k': 294.26},
                           {'kg_m_3': 874.29, 'ref_temp_k': 297.04},
                           {'kg_m_3': 871.40, 'ref_temp_k': 299.82},
                           {'kg_m_3': 868.36, 'ref_temp_k': 302.59},
                           {'kg_m_3': 865.48, 'ref_temp_k': 305.37},
                           {'kg_m_3': 862.43, 'ref_temp_k': 308.15},
                           {'kg_m_3': 859.55, 'ref_temp_k': 310.93},
                           {'kg_m_3': 856.51, 'ref_temp_k': 313.71},
                           {'kg_m_3': 853.62, 'ref_temp_k': 316.48},
                           {'kg_m_3': 850.58, 'ref_temp_k': 319.26},
                           {'kg_m_3': 847.70, 'ref_temp_k': 322.04},
                           {'kg_m_3': 844.65, 'ref_temp_k': 324.82},
                           {'kg_m_3': 841.61, 'ref_temp_k': 327.59},
                           {'kg_m_3': 838.73, 'ref_temp_k': 330.37},
                           {'kg_m_3': 835.68, 'ref_temp_k': 333.15},
                           {'kg_m_3': 832.80, 'ref_temp_k': 335.93},
                           {'kg_m_3': 829.76, 'ref_temp_k': 338.71},
                           {'kg_m_3': 826.87, 'ref_temp_k': 341.48},
                           {'kg_m_3': 823.83, 'ref_temp_k': 344.26},
                           {'kg_m_3': 820.95, 'ref_temp_k': 347.04},
                           {'kg_m_3': 817.90, 'ref_temp_k': 349.82},
                           {'kg_m_3': 814.86, 'ref_temp_k': 352.59},
                           ],
             'kvis': [{'m_2_s': 8.513e-7, 'ref_temp_k': 283.15},
                      {'m_2_s': 7.357e-7, 'ref_temp_k': 293.15},
                      {'m_2_s': 5.415e-7, 'ref_temp_k': 323.15},
                      {'m_2_s': 3.89e-7, 'ref_temp_k': 353.15},
                      ],
             'dvis': [
                      {'kg_ms': 7.24e-4, 'ref_temp_k': 285.93},
                      {'kg_ms': 6.93e-4, 'ref_temp_k': 288.71},
                      {'kg_ms': 6.65e-4, 'ref_temp_k': 291.48},
                      {'kg_ms': 6.38e-4, 'ref_temp_k': 294.26},
                      {'kg_ms': 6.12e-4, 'ref_temp_k': 297.04},
                      {'kg_ms': 5.88e-4, 'ref_temp_k': 299.82},
                      {'kg_ms': 5.66e-4, 'ref_temp_k': 302.59},
                      {'kg_ms': 5.44e-4, 'ref_temp_k': 305.37},
                      {'kg_ms': 5.24e-4, 'ref_temp_k': 308.15},
                      {'kg_ms': 5.05e-4, 'ref_temp_k': 310.93},
                      {'kg_ms': 4.87e-4, 'ref_temp_k': 313.71},
                      {'kg_ms': 4.70e-4, 'ref_temp_k': 316.48},
                      {'kg_ms': 4.53e-4, 'ref_temp_k': 319.26},
                      {'kg_ms': 4.38e-4, 'ref_temp_k': 322.04},
                      ],
             'molecular_weights': [{'sara_type': 'Aromatics',
                                    'g_mol': 78.11,
                                    'ref_temp_k': 353.45,
                                    },
                                   ],
             'sara_densities': [{'sara_type': 'Aromatics',
                                 'density': 814.0,
                                 'ref_temp_k': 353.45,
                                 },
                                ],
             'sara_fractions': [{'sara_type': 'Aromatics',
                                 'fraction': 1.0,
                                 'ref_temp_k': 353.45,
                                 },
                                ],
             }
